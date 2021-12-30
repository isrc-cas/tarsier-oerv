import koji
import os
import json
import para

pkginfo_filepath = para.pkginfo_filepath
rpminfo_filepath = para.rpminfo_filepath


def get_rpmlist(pkginfo_file, rpminfo_file):
    with open(pkginfo_file, 'r') as f:
        pkgsdata = json.load(f)
    session = koji.ClientSession("http://fedora.riscv.rocks/kojihub")
    pkg_rpmlist = []
    for pkgdata in pkgsdata:
        print ('package:', pkgdata['package'])
        if pkgdata['tagged'] == 'success':
           rpmlist = session.listRPMs(buildID=pkgdata['buildID'])
           newrpmlist = []
           count = 0
           for rpmdata in rpmlist:
               if rpmdata['arch'] != 'src':
                   count = count + 1
                   rpm_name = '{}.{}.rpm'.format(rpmdata['nvr'],rpmdata['arch'])
                   rpm_url = 'http://fedora.riscv.rocks/kojifiles/packages/{}/{}/{}/{}/{}'.format(pkgdata['package'],
                   rpmdata['version'],rpmdata['release'],rpmdata['arch'],rpm_name)
                   rpm_dic = dict(rpm_name=rpm_name, rpm_url=rpm_url)
                   newrpmlist.append(rpm_dic)
                #    print ('count:', count)
           pkgrpm_dic = dict(package=pkgdata['package'],rpm_count=count,rpmlist=newrpmlist,result=pkgdata['tagged'])
        else:
            pkgrpm_dic = dict(package=pkgdata['package'],rpm_count=0,rpmlist=[],result=pkgdata['tagged'])
        pkg_rpmlist.append(pkgrpm_dic)
    print ('package length', len(pkg_rpmlist))
    
    with open(rpminfo_file, 'w') as f:
        json.dump(pkg_rpmlist, f)

    

if __name__=="__main__":
    get_rpmlist(pkginfo_filepath, rpminfo_filepath)