import koji
import os
import json
import para


pkg_filepath = para.pkg_filepath
tag = para.tag
pkginfo_filepath = para.pkginfo_filepath

def get_package(pkg_file, tag, pkginfo_file):
    f = open(pkg_file, 'r')
    tagged_list = []
    session = koji.ClientSession("http://fedora.riscv.rocks/kojihub")
    count = 0
    for line in f.readlines(): 
        count = count + 1
        pkgname = line.replace('\n', '')
        print ('package:', pkgname)
        try:
            packageinfo = session.listTagged(tag=tag,latest=True,package=pkgname)
            result = 'success'
            dic = dict(package=packageinfo[0]['name'], buildID=packageinfo[0]['build_id'], tagged=result)
        except:
            result = 'fail'
            dic = dict(package=pkgname, buildID='none', tagged=result)
        tagged_list.append(dic)
    print ('get package length', len(tagged_list))
    print ('package length', count)
    
    with open(pkginfo_file, 'w') as f:
        json.dump(tagged_list, f)
        


if __name__=="__main__":
    get_package(pkg_filepath, tag, pkginfo_filepath)