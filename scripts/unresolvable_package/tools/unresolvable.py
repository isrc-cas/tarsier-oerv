#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#  cmd: python3 update.py xxx(such as 1912 unresolvable package total)

import os
import sys
import json
import time

work_dir=os.getcwd()+"/"
unresolvable_total=sys.argv[1]
file_date=time.strftime("%Y%m%d", time.localtime())
json_suffix="_"+str(unresolvable_total)+"_" +file_date+".json"
txt_suffix="_"+str(unresolvable_total)+"_" +file_date+".txt"

filepath =  work_dir + r'unresolvable_'+ str(unresolvable_total)+".json"
updatepath = work_dir + r'unresolvable_update'+json_suffix
name_path = work_dir + r'unresolvable_package' + txt_suffix
count_path = work_dir + r'unresolvable_package_count' + json_suffix

unresolvable_package_name=[]
deps_num_packages={}

def count_deps(deps):
  deps_nums={}
  for dep in deps:
    deps_nums[dep] = deps.count(dep)
  return deps_nums


def parse_deps(key,details):
  deps_num = 0
  deps = details.split(',')
  ret_deps = []
  one_dict = {}
  for dep in deps:
    if dep.strip().startswith("nothing provides"):
      ret_deps.append(dep.split()[2])
    elif dep.strip().startswith("have choice"):
      ret_deps.append(dep.split()[3])
    else:
      ret_deps.append(dep.strip())
    deps_num += 1
  if str(deps_num) in deps_num_packages:
    ret_deps.extend(deps_num_packages[str(deps_num)])
  one_dict[str(deps_num)] = ret_deps
  deps_num_packages.update(one_dict)
  return (deps_num,ret_deps)


after = []
with open(filepath, 'r') as f:
    data = json.load(f)
    for key in data.keys():
      unresolvable_package_name.append(key.strip()+"\n")
      mask=data[key]
      (num, deps) = parse_deps(key, mask["details"])
      mask["num"]=num
      mask["details"]=deps
    after = data

with open(updatepath, 'w') as f:
    data = json.dump(after, f,sort_keys=True, indent=4, separators=(',', ': '))

for key,value in deps_num_packages.items():
    deps_num_packages[key] = count_deps(value)

with open(count_path, 'w') as f:
    data = json.dump(deps_num_packages, f,sort_keys=True, indent=4, separators=(',', ': '))

# print(deps_num_packages)
# f = open('test.txt', 'w')
# f.write(str(dep_one))
# f.close()

f = open(name_path, 'w')
f.writelines(unresolvable_package_name)
f.close()
