import requests
import json
import re
import os
import constant
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl import worksheet
from openpyxl.styles import Side, Border
import time
import datetime

unresolvable_url = 'https://build.openeuler.org/project/monitor/openEuler:Mainline:RISC-V?arch_riscv64=1&defaults=0&repo_standard_riscv64=1&unresolvable=1'
succeeded_url = 'https://build.openeuler.org/project/monitor/openEuler:Mainline:RISC-V?arch_riscv64=1&defaults=0&repo_standard_riscv64=1&succeeded=1'
failed_url = 'https://build.openeuler.org/project/monitor/openEuler:Mainline:RISC-V?arch_riscv64=1&defaults=0&failed=1&repo_standard_riscv64=1'


def get_packagelist(url):
    response = requests.get(url)
    data = response.text
    datalist = data.split('\n')
    pacakgedatalist = [x for x in datalist if x.startswith('<tbody')]
    packagedata = pacakgedatalist[0].split("='")
    data_packagenames = packagedata[1].split("]'")[0].replace("[","").replace("&quot;","").split(", ")
    # tmp_data_statushash = packagedata[3].replace("&quot;","").replace("{standard_riscv64:{riscv64:","").replace("}}' data-tableinfo","")

    # packagelistdata = packagedata[1].replace('<tbody data-packagenames', '')
    # packagelistdata = packagelistdata.replace(' data-project', '')
    # packagelistdata = re.sub(r'&quot;', '', packagelistdata)
    # packagelistdata = re.sub(r' ', '', packagelistdata)
    # packagelist = packagelistdata[2:-2].split(',')
    # print (len(packagelist))
    return data_packagenames

# 定义状态对应的编号（用于excle数据分析和sheetindex）
def getCode(status):
    code = 3
    if status == 'succeeded':
        code = 0
    if status == 'unresolvable':
        code = 1
    if status == 'failed':
        code = 2

    return code

def writeToExcle(filepath, datelist, title):
    status = getCode(title)

    wb = load_workbook(filepath)
    # sheetindex = len(wb.worksheets)
    ws = wb.create_sheet(title, status)  #这里简单用status值代替sheetindex，偷个懒
    ws.append(['packagename','status'])
    ws.column_dimensions["A"].width = 20
    ws.column_dimensions["B"].width = 20

    for itPkgname in datelist:
        ws.append([itPkgname, status])

    print(title + "  is done!  file path is ：" + filepath)
    wb.save(filepath)


if __name__=="__main__":
    # 获取各状态下的packagesname
    unresolvable_packagelist = get_packagelist(unresolvable_url)
    succeeded_packagelist = get_packagelist(succeeded_url)
    failed_packagelist = get_packagelist(failed_url)

    # 根据日期新建excle，并写入数据。用于归档和数据分析用
    nowtime = time.strftime("%Y%m%d-%H%M", time.localtime())
    print(nowtime)
    sheetName = 'obsBuild-' + nowtime
    obsdatafolder = os.getcwd().replace("scripts\dependent_package",'data\obsBuildStatus')
    obsfilepath = os.path.join(obsdatafolder, sheetName+'.xlsx')

    wb = Workbook()
    wb.save(obsfilepath)

    # 写入数据到excle
    writeToExcle(obsfilepath, succeeded_packagelist, "succeeded")
    writeToExcle(obsfilepath, unresolvable_packagelist, "unresolvable")
    writeToExcle(obsfilepath, succeeded_packagelist, "failed")