import requests
import json
import base64
import re
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
buildrequire_filepath = os.path.join(os.getcwd(), 'buildrequiresfile.json')

def get_buildrequires(headers, params, specfile, requirefile):
    with open(specfile, 'r') as f:
        specdata = json.load(f)
    # print ('specdata length', len(specdata))
    requirepakcage_list = []
    for specfile in specdata:
        print ('specfile', specfile)
        response = requests.get(specfile['apiurl'], headers=headers, params=params)
        specfiledata = json.loads(response.text)
        # print (specfiledata)
        spec_content = base64.b64decode(specfiledata['content']).decode()
        # print ('spec_content', spec_content)
        specdata_list = spec_content.split('\n')
        # print ('specdata_list', specdata_list)
        namelist = [x for x in specdata_list if re.match('[Nn]ame *:', x)]
        namelist = [re.sub(r'\t', ' ', x) for x in namelist]
        namelist = [re.sub(r' ', '', x) for x in namelist]
        # print ('namelist', namelist)
        packagename = list(filter(None, namelist[0].split(':')))[1]
        print ('packagename', packagename)
        buildrequires = [x for x in specdata_list if x.startswith('BuildRequires:')]
        buildrequires = [x.replace('BuildRequires:', 'BuildRequires: ') for x in buildrequires]
        buildrequires = [re.sub(r'\t', ' ', x) for x in buildrequires]
        print ('buildrequire', buildrequires)
        requirespkg_list = []
        for item in buildrequires:
            itemlist = list(filter(None, item.split(' ')))
            print ('itemlist', itemlist)
            for i in range(len(itemlist)):
                # print ('itemlist[i]', itemlist[i])
                m1 = re.match(r'^[^A-Za-z0-9_/-]*', itemlist[i]).group()
                m2 = re.match(r'^(\d\W)*', itemlist[i]).group()
                # print ('match string1', m1)
                # print ('match string2', m2)
                if m1 or m2:
                    itemlist[i] = ''
            itemlist.remove('BuildRequires:')
            itemlist = list(filter(None, itemlist))
            # print ('newitemlist', itemlist)
            requirespkg_list = requirespkg_list + itemlist
        # print ('requirespkg_list', requirespkg_list)
        requirespkg_dict = dict(package=specfile['package'], packagename=packagename, buildrequires=requirespkg_list)
        print ('requirespkg_dict', requirespkg_dict)
        requirepakcage_list.append(requirespkg_dict)
        print ('requirepakcage_list length', len(requirepakcage_list))
    print ('requirepakcage_list length', len(requirepakcage_list))
    with open(requirefile, 'w') as f:
        json.dump(requirepakcage_list, f)


if __name__=="__main__":
    get_buildrequires(headers, params, specfilepath, buildrequire_filepath)