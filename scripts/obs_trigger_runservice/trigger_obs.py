import requests
from requests.auth import HTTPBasicAuth
import parameters
import sys
import re
import time



def get_usertoken(url, account):
    token_url = '{}/person/{}/token'.format(url, account['username'])
    token_resp = requests.get(token_url, auth=HTTPBasicAuth(account['username'],account['password']))
    # print ('get token resp status code>>>', token_resp.status_code)
    # print ('get token resp token text>>>', token_resp.text)
    # print ('token count>>>', re.findall('count="0"', token_resp.text))
    if len(re.findall('count="0"', token_resp.text)) == 0:
        # print ('tokeninforstr>>>', re.findall('id=".*" kind=', token_resp.text))
        tokeninfo_list = []
        for tokeninfostr in re.findall('id=".*" kind=', token_resp.text):
            tokenid = int(re.search('id=".*" string=', tokeninfostr).group()[4:-9])
            token = re.search('string=".*" kind=', tokeninfostr).group()[8:-7]
            tokeninfo = {'id': tokenid, 'token': token}
            # print ('tokeninfo>>>', tokeninfo)
            tokeninfo_list.append(tokeninfo)
        # print ('tokeninfo_list>>>', tokeninfo_list)
    else:
        # print ('cannot find token in obs')
        tokeninfo_list = []
    return tokeninfo_list


def post_usertoken(url, account, token):
    post_token_url = '{}/person/{}/token'.format(url, account['username'])
    token_data = {'operation': 'runservice', 'scm_token': token} 
    post_token_resp = requests.post(post_token_url, auth=HTTPBasicAuth(account['username'],account['password']), data=token_data)
    # print ('post token resp status code>>>', post_token_resp.status_code)
    # print ('post token resp text>>>', post_token_resp.text)


def delete_token(url, account, id):
    delete_token_url = '{}/person/{}/token/{}'.format(url, account['username'], id)
    delete_token_resp = requests.delete(delete_token_url, auth=HTTPBasicAuth(account['username'],account['password']))
    # print ('delete token resp status code>>>', delete_token_resp.status_code)
    # print ('delete token resp text>>>', delete_token_resp.text)


def trigger_package(project, package, url, account, token):
    trigger_url = '{}/trigger/runservice'.format(url)
    pkginfo = {'project': project, 'package': package}
    header = {'Authorization': 'Token {}'.format(token)}
    trigger_pkg_resp = requests.post(trigger_url, headers=header, data=pkginfo)
    # print ('trigger package resp status code>>>', trigger_pkg_resp.status_code)
    # print ('trigger package resp text>>>', trigger_pkg_resp.text)
    if trigger_pkg_resp.status_code == 200:
        print ('{} trigger runservice successfully'.format(package)) 
    else:
        print ('{} trigger runservice unsuccessfully, please check it'.format(package))


def get_packages(url, account, project):
    get_packages_url = '{}/source/{}'.format(url, project)
    get_packages_resp = requests.get(get_packages_url,auth=HTTPBasicAuth(account['username'],account['password']))
    # print ('get packages resp status code>>>', get_packages_resp.status_code)
    # print ('get packages resp text>>>', get_packages_resp.text)
    packagelist = [pkg[6:-1] for pkg in re.findall('name=".*"', get_packages_resp.text)]
    # print ('packagelist>>>', packagelist)
    return packagelist




if __name__=="__main__":
    obs_account = parameters.obs_account
    obs_url = parameters.obs_url
    gitee_token = parameters.gitee_token
    if len(sys.argv) == 1:
        print ('obs project is required')
    elif len(sys.argv) == 2:
        print ('trigger all packages of obs project {}'.format(sys.argv[1]))
        packagelist = get_packages(obs_url, obs_account, sys.argv[1])
        tokenlist = get_usertoken(obs_url, obs_account)
        if len(tokenlist) > 0:
            for tokeninfo in tokenlist:
                delete_token(obs_url, obs_account, tokeninfo['id'])
        post_usertoken(obs_url, obs_account, gitee_token)
        tokenlist_new = get_usertoken(obs_url, obs_account)
        # print ('tokenlist_new>>>', tokenlist_new)
        for pkg in packagelist:
            trigger_package(sys.argv[1], pkg, obs_url, obs_account, tokenlist_new[0]['token'])
            time.sleep(1)
        delete_token(obs_url, obs_account, tokenlist_new[0]['id'])
        get_usertoken(obs_url, obs_account)
    elif len(sys.argv) == 3:
        print ('trigger the specified package {} of the project {}'.format(sys.argv[1], sys.argv[2]))
        tokenlist = get_usertoken(obs_url, obs_account)
        if len(tokenlist) > 0:
            for tokeninfo in tokenlist:
                delete_token(obs_url, obs_account, tokeninfo['id'])
        post_usertoken(obs_url, obs_account, gitee_token)
        tokenlist_new = get_usertoken(obs_url, obs_account)
        trigger_package(sys.argv[1], sys.argv[2], obs_url, obs_account, tokenlist_new[0]['token'])
        delete_token(obs_url, obs_account, tokenlist_new[0]['id'])
        get_usertoken(obs_url, obs_account) 
    else:
        print ('python command parameters error')
      


    
   
