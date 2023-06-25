import requests
from requests.auth import HTTPBasicAuth
import parameters
import sys


def rebuild_package(url, account, project, packages):
    get_buildresult_url = '{}/build/{}?cmd=rebuild'.format(url, project)
    post_data = {
        'package': packages, 
        'repository': obs_buildinfo['repo'], 
        'arch': obs_buildinfo['arch']
        }
    # print (post_data)
    post_rebuild_resp = requests.post(get_buildresult_url, auth=HTTPBasicAuth(account['username'],account['password']), data=post_data)
    print ('rebuild resp status_code>>>', post_rebuild_resp.status_code)
    print ('rebuild resp text>>>', post_rebuild_resp.text)


if __name__=="__main__":
   obs_account = parameters.obs_account
   obs_url = parameters.obs_url
   obs_project = parameters.obs_project
   obs_buildinfo = parameters.obs_buildinfo
   obs_packagelist = parameters.obs_packagelist
   rebuild_package(obs_url, obs_account, obs_project, obs_packagelist)