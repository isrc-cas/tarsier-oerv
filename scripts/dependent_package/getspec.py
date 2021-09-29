#!/usr/bin/env python3
# -*-coding:utf-8-*-

import requests
import json
import os
import constant

token = constant.token
headers = {
    'Content-Type': 'application/json;charset=UTF-8'
    }
params = {
    'access_token': token
}

specfilepath = os.path.join(os.getcwd(), 'specfile.json')


# 从obs获取所有包名
def get_packagelist():
    allpkgNameList = []

    # 本链接地址是从obs-overview中抓取的，将默认的求包数量100改成了5000（取了一个大数让所有数据一次性返回）
    linkaddress = 'https://build.openeuler.org/package?project=openEuler:Mainline:RISC-V' \
                  '&draw=1&columns[0][data]=name&columns[0][name]=' \
                  '&columns[0][searchable]=true' \
                  '&columns[0][orderable]=true' \
                  '&columns[0][search][value]=' \
                  '&columns[0][search][regex]=false' \
                  '&columns[1][data]=changed' \
                  '&columns[1][name]=&columns[1][searchable]=true' \
                  '&columns[1][orderable]=true&columns[1][search][value]=' \
                  '&columns[1][search][regex]=false&order[0][column]=0&order[0][dir]=asc' \
                  '&start=0&length=5000' \
                  '&search[value]=&search[regex]=false&_=1631946706374'
    response = requests.get(linkaddress)
    data = json.loads(response.text)
    print(data['recordsTotal'])

    datapkgs = data['data']
    for pkg in datapkgs:
        name = pkg['name'].split('">')[1].split('<')[0]
        allpkgNameList.append(name)

    return allpkgNameList


# 从obs_meta/openEuler:Mainline:RISC-V中获取仓库所有的包
def get_packages(headers, params):
    url = 'https://gitee.com/api/v5/repos/openEuler/RISC-V/contents/configuration/obs_meta/openEuler:Mainline:RISC-V'
    response = requests.get(url, headers=headers, params=params)
    packages = json.loads(response.text)
    #print ('packages length', len(packages))   #1001个
    packagelist = [x['name'] for x in packages]
    #print ('packagelist length', len(packagelist))
    return packagelist


def get_specfile(headers, params, packages, filepath):
    specfile_list = []
    nopkg_list = []
    for pkg in packages:
        if pkg == 'rubygems-ronn':
            pkg = 'rubygem-ronn'
        if pkg == 'appstream-data':
            pkg = 'appstream'
        url = 'https://gitee.com/api/v5/repos/src-openEuler/{}/contents'.format(pkg)
        # https://gitee.com/api/v5/repos/openeuler/RISC-V/contents/configuration/obs_meta/openEuler:Mainline:RISC-V/A-Tune/_service
        # url = 'https://gitee.com/api/v5/repos/src-openEuler/args4j/contents'
        # print('url=',url)

        # 在content中查询spec文件，并获取其url（content的内容与obs包的文件列表对应，参考contents.json）
        response = requests.get(url, headers=headers, params=params)
        packagesource = json.loads(response.text)
        if type(packagesource).__name__ == 'dict':
            nopkg_list.append(pkg)
            print('Not Found Project:', pkg, len(nopkg_list))
        if type(packagesource).__name__ == 'list':
            specfiles = [x['name'] for x in packagesource if x['name'].endswith('.spec')]
            # print ('specfiles', specfiles)

            for spec in specfiles:
                specfile_api = 'https://gitee.com/api/v5/repos/src-openEuler/{}/contents/{}'.format(pkg, spec)
                # print ('specfile_api:',specfile_api)
                specfile_dict = dict(package=pkg, specfile=spec, apiurl=specfile_api)
                specfile_list.append(specfile_dict)
            # print ('specfile_list length', len(specfile_list))
            print('Project:', pkg, len(specfile_list))

            # 将一个包的包名、specurl等信息写入到本地的specfile.json文件。单包格式：{"package": "A-Tune", "specfile": "atune.spec", "apiurl": "https://gitee.com/api/v5/repos/src-openEuler/A-Tune/contents/atune.spec"}
            filepath = os.path.join(os.getcwd(), 'specfile.json')
            with open(specfilepath, 'w') as f:
                json.dump(specfile_list, f)
                # print(pkg, ' is writting....')

    print('Done!   Not Found Project:', ';'.join(nopkg_list))


if __name__=="__main__":
    # packagelist = get_packages(headers, params)
    packagelist = get_packagelist()
    get_specfile(headers, params, packagelist, specfilepath)
