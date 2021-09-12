import requests
import json
import re
import os

unresolvable_url = 'https://build.openeuler.org/project/monitor/openEuler:Mainline:RISC-V?arch_riscv64=1&defaults=0&repo_standard_riscv64=1&unresolvable=1'

succeeded_url = 'https://build.openeuler.org/project/monitor/openEuler:Mainline:RISC-V?arch_riscv64=1&defaults=0&repo_standard_riscv64=1&succeeded=1'

packaglistfilepath = os.path.join(os.getcwd(), 'packagelist.json')

def get_packagelist(url):
    response = requests.get(url)
    data = response.text
    datalist = data.split('\n')
    pacakgedatalist = [x for x in datalist if x.startswith('<tbody')]
    packagedata = pacakgedatalist[0].split('=')
    packagelistdata = packagedata[1].replace('<tbody data-packagenames', '')
    packagelistdata = packagelistdata.replace(' data-project', '')
    packagelistdata = re.sub(r'&quot;', '', packagelistdata)
    packagelistdata = re.sub(r' ', '', packagelistdata)
    packagelist = packagelistdata[2:-2].split(',')
    print (len(packagelist))
    return packagelist



if __name__=="__main__":
    unresolvable_packagelist = get_packagelist(unresolvable_url)
    succeeded_packagelist = get_packagelist(succeeded_url)
    packagelist_dict = dict(unresolvable=unresolvable_packagelist, succeeded=succeeded_packagelist)
    with open(packaglistfilepath, 'w') as f:
        json.dump(packagelist_dict, f)
    