import requests
import re
import openpyxl
import configparser



def getPageNum(keyword):
    url='https://gitee.com/organizations/src-openeuler/projects?search='+keyword+'&lang_id=&type=&status=&_=1650935152426'
    response=requests.get(url)
    data=response.text
    #print(data)

    pageNum=re.findall('class=\"item\".*?page=(\\d+)&amp;search='+keyword,data)[-1]
    print (pageNum)
    return pageNum

def getPackagePerPage(keyword,pageID):
    url='https://gitee.com/organizations/src-openeuler/projects?_=1650935152428&lang_id=&page='+str(pageID)+'&search='+keyword+'&status=&type='
    
    config=configparser.RawConfigParser()
    config.read('config.ini',encoding='utf-8-sig')
    cookie=config.get('default','gitee_cookie')
    headers = {
        "cookie": cookie
        }
    

    response=requests.get(url,headers=headers)
    data=response.text
    #print(data)
    packageList=re.findall('href=\"/src-openeuler/(.*?'+keyword+'.*?)/watchers"><i class=\'iconfont icon-watch\'>',data,re.IGNORECASE)
    print (packageList)
    #print (len(packageList))
    return packageList

def recordPackage(ws,packageList):
    
    for package in packageList:
        ws.append([package])


if __name__=='__main__':
    config=configparser.ConfigParser(interpolation=configparser.BasicInterpolation())
    config.read('config.ini',encoding='utf-8-sig')
    keyword=config.get('default','target_package')

    recordFileName=config.get('default','record_file')
    print ("will save to "+recordFileName)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['PackageName'])

    pageNum=int(getPageNum(keyword))
    for pageID in range(1,pageNum+1):
        print('Now getting page:'+str(pageID)+' package')
        packageList=getPackagePerPage(keyword,pageID)
        if pageID!=pageNum and len(packageList)!=20:
            raise Exception ('error')
        recordPackage(ws,packageList)
    
    wb.save(recordFileName)
