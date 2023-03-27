import requests
import parameters
from requests.auth import HTTPBasicAuth
import re
import os
import shutil
from lxml import etree


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


def download_servicefile(url, account, project, filedir, packagelist):
    for pkg in packagelist:
        get_service_url = '{}/source/{}/{}/_service'.format(url, project, pkg)
        get_service_resp = requests.get(get_service_url,auth=HTTPBasicAuth(account['username'],account['password']))
        # print (get_service_resp.text,get_service_resp.status_code)
        if get_service_resp.status_code == 200:
           servicefiledir = os.path.join(filedir, pkg)
           os.mkdir(servicefiledir)
           servicefilepath = os.path.join(servicefiledir, '_service')
           with open(servicefilepath, 'w') as f:
               f.write(get_service_resp.text)
           print ('download {} _service file successfully'.format(pkg))
        else:
            print ('download {} _service file unsuccessfully'.format(pkg))


def download_specfile(url, account, project, filedir, packagelist):
    for pkg in packagelist:
        get_spec_url = '{}/package/view_file/{}/{}/_service:tar_scm:{}.spec?expand=1'.format(url, project, pkg, pkg)
        get_spec_resp = requests.get(get_spec_url,auth=HTTPBasicAuth(account['username'],account['password']))
        # print (get_spec_resp.text, get_spec_resp.status_code)
        if get_spec_resp.status_code == 200:
            html = etree.HTML(get_spec_resp.text)
            content = etree.tostring(html).decode()
            # print ('content>>>', content)
            pattern = '<textarea name="editor_0" id="editor_0" cols="0" rows="0" class="form-control">((.|\n)*)</textarea>'
            # print (re.search(pattern, content).group(1))
            specfilepath = os.path.join(filedir, '{}.spec'.format(pkg))
            with open(specfilepath, 'w') as f:
                f.write(re.search(pattern, content).group(1))
            print ('download {} spec file successfully'.format(pkg))
        else:
            print ('download {} spec file unsuccessfully'.format(pkg))




if __name__=="__main__":
   obs_account = parameters.obs_account
   obs_url = parameters.obs_url
   obs_project = parameters.obs_project
   filetype = parameters.filetype
   if filetype == 'service':
      filedir = os.path.join(os.getcwd(), 'servicefile')
      if os.path.exists(filedir):
          shutil.rmtree(filedir)
      os.mkdir(filedir)
      pkglist = get_pkgs(obs_url, obs_account, obs_project, filedir)
      download_servicefile(obs_url, obs_account, obs_project, filedir, pkglist)
   elif filetype == 'spec':
       filedir = os.path.join(os.getcwd(), 'specfile')
       if os.path.exists(filedir):
          shutil.rmtree(filedir)
       os.mkdir(filedir)
       pkglist = get_pkgs(obs_url, obs_account, obs_project, filedir)
       download_specfile(obs_url, obs_account, obs_project, filedir, pkglist)
   else:
        print ('file type error')
      
      