import requests
import parameters
from requests.auth import HTTPBasicAuth
import os


def get_pkgs():
    filedir = os.path.join(os.getcwd(), 'pkgs.txt')
    pkglist = []
    with open(filedir, 'r') as f:
        for line in f.readlines():
            pkg = line.strip('\n')
            pkglist.append(pkg)
    print ('pkglist>>>', pkglist)
    return pkglist


def set_pkg_tag(url, account, project, repolist, post_data, pkglist):
    for pkg in pkglist:
        set_tag_url = '{}/source/{}/{}?cmd=set_flag'.format(url, project, pkg)
        for repo in repolist:
            post_data['repository'] = repo
            set_tag_resp = requests.post(set_tag_url, auth=HTTPBasicAuth(account['username'],account['password']), data=post_data)
            # print (set_tag_resp.text, set_tag_resp.status_code)
            if set_tag_resp.status_code == 200:
                print ('{} {} repo {} flag set flag successfully'.format(pkg, post_data['repository'], post_data['flag']))
            else:
                print ('{} {} repo {} flag set flag unsuccessfully'.format(pkg, post_data['repository'], post_data['flag']))



if __name__=="__main__":
   pkglist = get_pkgs()
   obs_account = parameters.obs_account
   obs_url = parameters.obs_url
   obs_project = parameters.obs_project
   obs_repolist = parameters.obs_repolist
   obs_post_data = parameters.obs_post_data
   set_pkg_tag(obs_url, obs_account, obs_project, obs_repolist, obs_post_data, pkglist)

