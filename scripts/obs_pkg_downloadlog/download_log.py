import requests
import parameters
from requests.auth import HTTPBasicAuth
import os
import sys
import shutil


def download_logfile(url, account, project, buildinfo, pkglist, filedir):
    for pkg in pkglist:
        get_log_url = '{}/build/{}/{}/{}/{}/_log'.format(url, project, buildinfo['repo'], buildinfo['arch'], pkg)
        get_log_resp = requests.get(get_log_url,auth=HTTPBasicAuth(account['username'],account['password']))
        # print (get_log_resp.text, get_log_resp.status_code)
        if get_log_resp.status_code == 200:
            logfiledir = os.path.join(filedir, pkg)
            os.mkdir(logfiledir)
            logfilepath = os.path.join(logfiledir, '_log')
            with open(logfilepath, 'w') as f:
                f.write(get_log_resp.text)
            print ('download {} _log file successfully'.format(pkg))
        else:
            print ('download {} _log file unsuccessfully'.format(pkg))
            failedfilepath = os.path.join(filedir, 'download_failed_recorder.txt')
            with open(failedfilepath, 'a') as f:
                f.write('download {} _log file unsuccessfully\n'.format(pkg))


if __name__=="__main__":
    obs_account = parameters.obs_account
    obs_url = parameters.obs_url
    obs_project = parameters.obs_project
    obs_buildinfo = parameters.obs_buildinfo
    pkglist = parameters.obs_packagelist
    filedir = os.path.join(os.getcwd(), 'logfile')
    if os.path.exists(filedir):
        shutil.rmtree(filedir)
    os.mkdir(filedir)
    if len(pkglist) > 0:
       download_logfile(obs_url, obs_account, obs_project, obs_buildinfo, pkglist, filedir)
    else:
        print ('please enter package name to be downloaded in parameters.py')