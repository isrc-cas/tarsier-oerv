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

base_url = 'https://build.openeuler.org/project/monitor/openEuler:Mainline:RISC-V?arch_riscv64=1&defaults=0&repo_standard_riscv64=1'

def get_packagelist(url):
    response = requests.get(url)
    data = response.text
    datalist = data.split('\n')
    pacakgedatalist = [x for x in datalist if x.startswith('<tbody')]
    packagedata = pacakgedatalist[0].split("='")
    data_packagenames = packagedata[1].split("]'")[0].replace("[","").replace("&quot;","").split(", ")

    return data_packagenames

# 定义状态对应的编号（用于excle数据分析和sheetindex）
def getCode(status):
    code = 6
    if status == 'succeeded':
        code = 0
    if status == 'failed':
        code = 1
    if status == 'unresolvable':
        code = 2
    if status == 'broken':
        code = 3
    if status == 'disabled':
        code = 4
    if status == 'excluded':
        code = 5

    return code

def writeToExcle(filepath, datelist, dt, title):
    wb = load_workbook(filepath)

    # 记录统计数据
    wst = wb.worksheets[0]
    wst.append([dt, title, len(datelist)])

    # 记录详细数据
    ws = wb[dt]
    for itPkgname in datelist:
        ws.append([itPkgname, getCode(title), title])

    print(title + ": ",len(datelist))
    wb.save(filepath)



if __name__=="__main__":
    # 根据日期新建excle，并写入数据。用于归档和数据分析用
    nowtime = time.strftime("%Y%m%d-%H%M", time.localtime())
    print(nowtime)
    sheetName = 'obsBuild'
    obsdatafolder = os.getcwd().replace("scripts\dependent_package",'data\obsBuildStatus')
    obsfilepath = os.path.join(obsdatafolder, sheetName+'.xlsx')

    try:
        wb = load_workbook(obsfilepath)
        ws = wb['buildresultsTotal']
    except FileNotFoundError:
        wb = Workbook()
        wst = wb.create_sheet("buildresultsTotal", 0)  #记录统计信息
        wst.append(['datetime','statusname','totalnum'])
        wst.column_dimensions["A"].width = 20
        wst.column_dimensions["B"].width = 20
        wst.column_dimensions["C"].width = 20

    sheetindex = len(wb.worksheets)
    ws = wb.create_sheet(nowtime, sheetindex)  #按日期记录详细构建信息
    ws.append(['packagename', 'statuscode', 'statusname'])
    ws.column_dimensions["A"].width = 20
    ws.column_dimensions["B"].width = 20
    ws.column_dimensions["C"].width = 20

    wb.save(obsfilepath)

    # # 获取各状态下的packagesname并写入数据到excle
    queryDate = ["succeeded","failed","unresolvable","broken","disabled","excluded"]
    for qd in queryDate:
        url = base_url+"&"+qd+"=1"
        # print(qd,"url=",url)
        packagelist = get_packagelist(url)
        writeToExcle(obsfilepath, packagelist, nowtime, qd)

    print('All datas in file ：', obsfilepath)