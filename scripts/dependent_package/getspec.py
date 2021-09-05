import requests
import json
import os


headers = {
    'Content-Type': 'application/json;charset=UTF-8'
    }
params = {
    'access_token': '1ff56996299ca3abb99cdbc2043401de'
}

specfilepath = os.path.join(os.getcwd(), 'specfile.json')

def get_packages(headers, params):
    url = 'https://gitee.com/api/v5/repos/openEuler/RISC-V/contents/configuration/obs_meta/openEuler:Mainline:RISC-V'
    response = requests.get(url, headers=headers, params=params)
    packages = json.loads(response.text)
    # print ('packages length', len(packages))
    packagelist = [x['name'] for x in packages]
    print ('packagelist length', len(packagelist))
    return packagelist


def get_specfile(headers, params, packages, filepath):
    specfile_list = []
    for pkg in packages:
        print ('package', pkg, packages.index(pkg)+1)
        if pkg == 'rubygems-ronn':
           pkg = 'rubygem-ronn'
        url = 'https://gitee.com/api/v5/repos/src-openEuler/{}/contents'.format(pkg)
        response = requests.get(url, headers=headers, params=params)
        packagesource = json.loads(response.text)
        specfiles = [x['name'] for x in packagesource if x['name'].endswith('.spec')]
        print ('specfiles', specfiles)
        for spec in specfiles:
            specfile_api = 'https://gitee.com/api/v5/repos/src-openEuler/{}/contents/{}'.format(pkg, spec)
            specfile_dict = dict(package=pkg, specfile=spec, apiurl=specfile_api)
            specfile_list.append(specfile_dict)
        print ('specfile_list length', len(specfile_list))
        filepath = os.path.join(os.getcwd(), 'specfile.json')
        with open(filepath, 'w') as f:
            json.dump(specfile_list, f)



if __name__=="__main__":
    packagelist = get_packages(headers, params)
    get_specfile(headers, params, packagelist, specfilepath)
