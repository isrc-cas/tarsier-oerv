import requests
import parameters
from requests.auth import HTTPBasicAuth
import re
import os
import shutil

def get_pkgs(url, account, project, filedir):
    get_pkgs_url = '{}/source/{}'.format(url, project)
    get_pkgs_resp = requests.get(get_pkgs_url, auth=HTTPBasicAuth(account['username'],account['password']))
    # print (get_pkgs_resp.text)
    pkgs = re.findall('entry name=".*"', get_pkgs_resp.text)
    # print ('pkgs', pkgs)
    pkglist = [re.search('entry name="(.*)"', pkg).group(1) for pkg in pkgs]
    # print ('pkglist', pkglist)
    # print ('pkglist length', len(pkglist))
    pkglist_path = os.path.join(filedir, 'packagelist.txt')
    with open(pkglist_path, 'w') as f:
        for pkg in pkglist:
            f.write(pkg + '\n')
    return pkglist


def download_servicefile(url, account, project, firdir, packagelist):
    # pkg = 'aalib'
    for pkg in packagelist:
        print ('downloading {}'.format(pkg))
        get_service_url = '{}/source/{}/{}/_service'.format(url, project, pkg)
        get_service_resp = requests.get(get_service_url,auth=HTTPBasicAuth(account['username'],account['password']))
        # print (get_service_resp.text)
        servicefiledir = os.path.join(filedir, pkg)
        os.mkdir(servicefiledir)
        servicefilepath = os.path.join(servicefiledir, '_service')
        with open(servicefilepath, 'w') as f:
            f.write(get_service_resp.text)



if __name__=="__main__":
   obs_account = parameters.obs_account
   obs_url = parameters.obs_url
   obs_project = parameters.obs_project
   filedir = os.path.join(os.getcwd(), 'servicefile')
   if os.path.exists(filedir):
        shutil.rmtree(filedir)
   os.mkdir(filedir)
   pkglist = get_pkgs(obs_url, obs_account, obs_project, filedir)
   download_servicefile(obs_url, obs_account, obs_project, filedir, pkglist)
