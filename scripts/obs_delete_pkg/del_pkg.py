import requests
from requests.auth import HTTPBasicAuth
import parameters
import os
import sys
import re


def get_pkgsfile(pkgsfile):
    filedir = os.path.join(os.getcwd(), pkgsfile)
    try:
        with open(filedir, 'r') as f:
           pkglist = [line.replace('\n', '') for line in f.readlines()]
        print ('pkglist>>>', pkglist)
        return pkglist
    except:
        print ('Not found such file or directory')
        sys.exit(1)
    
def get_pkgs(url, account, project):
    get_pkgs_url = '{}/source/{}'.format(url, project)
    get_pkgs_resp = requests.get(get_pkgs_url,auth=HTTPBasicAuth(account['username'],account['password']))
    # print ('get packages resp status code>>>', get_pkgs_resp.status_code)
    # print ('get packages resp text>>>', get_pkgs_resp.text)
    if get_pkgs_resp.status_code == 200:
       pkgs = re.findall('entry name=".*"', get_pkgs_resp.text)
       pkglist = [re.search('entry name="(.*)"', pkg).group(1) for pkg in pkgs]
    #    print ('pkglist', pkglist)
    #    print ('pkglist length', len(pkglist))
       return pkglist
    else:
        print ('Get the packages unsuccessfully')
        sys.exit(1)

def delete_pkgs(url, account, project, pkglist):
    for pkg in pkglist:
        del_pkg_url = '{}/source/{}/{}'.format(url, project, pkg)
        del_pkg_resp = requests.delete(del_pkg_url, auth=HTTPBasicAuth(account['username'],account['password']))
        # print ('del_pkg_resp.status_code', del_pkg_resp.status_code)
        if del_pkg_resp.status_code == 200:
            print ('{} delete ok'.format(pkg))
        else:
            print ('{} delete error'.format(pkg))



if __name__=="__main__":
   obs_account = parameters.obs_account
   obs_url = parameters.obs_url
#    print (len(sys.argv))
   if len(sys.argv) == 1:
      print ('Project is required')
   elif len(sys.argv) == 2:
      if not sys.argv[1].endswith('.txt'):
        obs_project = sys.argv[1]
        pkglist = get_pkgs(obs_url, obs_account, obs_project)
        if len(pkglist) > 0:
            delete_pkgs(obs_url, obs_account, obs_project, pkglist)
        else:
            print ('There is no package in the project')
      else:
        print ('Arguments error, Project is required')
   elif len(sys.argv) == 3:
      if (not sys.argv[1].endswith('.txt')) and (sys.argv[2].endswith('.txt')):
        obs_project = sys.argv[1]
        pkgsfile = sys.argv[2]
        # print ('obs_project,pkgsfile>>>', obs_project, pkgsfile)
        pkglist = get_pkgsfile(pkgsfile)
        if len(pkglist) > 0:
           delete_pkgs(obs_url, obs_account, obs_project, pkglist) 
        else:
            print ('There is no package in package list file')
      else:
        print ('Arguments error, please enter the correct arguments')
         
   
