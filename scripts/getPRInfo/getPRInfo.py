
import requests
import re
import configparser
import datetime
import os


def parseWatchList():
    pullIdList=[]
    filename=getConfig("default", "dir")+getConfig("default", "watchList")
    with open(filename,mode='r') as F:
        list=F.readlines()
        for url in list:
            try:
                pullId=re.search("pulls/(\\d+)",url).group(1)
                pullIdList.append(pullId)
            except:
                print("can't find pull id in "+url)
                continue

    return pullIdList

def getConfig(section,option):
    configFile=os.path.dirname(os.path.abspath(__file__))+"/config.ini"
    config = configparser.ConfigParser()
    config.read(configFile, encoding="utf-8")
    return config.get(section, option)

def getPRInfo(pullId):
    PRInfo={}

    #get PR info
    prefix=getConfig("default", "url")
    token=getConfig("default", "token")
    url = prefix+pullId+"?access_token="+token
    print("Get "+url+"...")

    r=requests.get(url).json()
    #print(r)
    PRInfo['title']=r['title']
    PRInfo['state']=r['state']

    #get PR comment
    url=prefix+pullId+"/comments?access_token="+token+"&page=1&per_page=20&direction=desc"
    print("Get " + url + "...")
    r = requests.get(url).json()
    #print(r)
    num=0
    for e in r:
        if e['user']['login']=='openeuler-ci-bot':
            #print(e['user']['login'])
            continue
        else:
            if 'lastCommentHuman' not in PRInfo.keys():
                PRInfo['lastCommentHuman']=e['user']['login']
                PRInfo['lastComment']=e['body'].replace("\n", "")
            updateTime=e['updated_at']
            updateTime=re.search('(.*)\\+08:00',updateTime).group(1)
            updateTime=updateTime.replace('T',' ')
            updateTime=datetime.datetime.strptime(updateTime, '%Y-%m-%d %H:%M:%S')
            #print(updateTime)
            now=datetime.datetime.now()
            if (now-updateTime).days<1:
                num+=1
    PRInfo['commentsInOneDay']=num
    return PRInfo

def getPRInfoInWatchList():
    pullList = parseWatchList()
    now=datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    resultFile=getConfig("default", "dir")+"result_"+now+".txt"
    f = open(resultFile, 'w+')
    f.write("PR_ID    PR_title    PR_state    lastCommentHuman    lastComment    commentsInOneDay\n")
    print("Will get PRlist " + str(pullList) + " info")
    for id in pullList:
        PRInfo = getPRInfo(id)
        f.write(
            id + "    " + PRInfo['title'] + "    " + PRInfo['state'] + "    " + PRInfo['lastCommentHuman'] + "    " +
            PRInfo['lastComment'] + "    " + str(PRInfo['commentsInOneDay']) + "\n")
    f.close()


if __name__=="__main__":
    getPRInfoInWatchList()
