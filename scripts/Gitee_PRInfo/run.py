import requests
import os
from openpyxl import Workbook
from openpyxl import load_workbook
import json
import constant
from openpyxl.styles import Side, Border


headers = {
    'Content-Type': 'application/json;charset=UTF-8'
    }

openEulerrepo_url = 'https://gitee.com/api/v5/repos/openeuler/RISC-V/pulls'

report_header = ['Title', 'URL', 'State']

token = constant.token
filepath = os.path.join(os.getcwd(), 'pr_info.xlsx')

def get_repoPRInfo(headers,token,url):
    i = 1
    PRInfolist = []
    while True:
        params = {
            'access_token': token,
            'state': 'all',
            'page': i,
            'per_page': 100
        }
        response = requests.get(url, headers=headers, params=params)
        data = json.loads(response.text)
        # print ('PRInfo data', len(data))
        if len(data) > 0:
            for item in data:
                pr_url = item['url'].replace('gitee.com/api/v5/repos/', 'gitee.com/', 1)
                PRInfo = [item['title'], pr_url, item['state']]
                PRInfolist.append(PRInfo)
            i = i + 1
        else:
            break
    # print ('PRInfolist', len(PRInfolist))
    return PRInfolist

def get_openEulerorg(headers, token):
    url = 'https://gitee.com/api/v5/orgs/openEuler-RISC-V/repos'
    i = 1
    repourllist = []
    while True:
        params = {
            'access_token': token,
            'page': i,
            'per_page': 100
        }
        response = requests.get(url, headers=headers, params=params)
        data = json.loads(response.text)
        # print ('org data', len(data))
        if len(data) > 0:
            for item in data:
               repourllist.append(item['url'])
            i = i + 1
        else:
            break
    # print ('repourllist', len(repourllist))
    return repourllist

def get_openEulerriscvPRInfo(headers, token, repourllist):
    PRInfodata = []
    for repourl in repourllist:
        url = '{}/pulls'.format(repourl)
        PRInfolist = get_repoPRInfo(headers,token,url)
        PRInfodata = PRInfodata + PRInfolist
    # print ('PRInfodata', len(PRInfodata))
    return PRInfodata
        

def create_excel(filepath, openEuler_PR, openEulerriscv_PR, header):
    wb = Workbook()
    ws = wb.active

    ws.title = "openeuler RISC-V repo PR"
    wb.create_sheet("openEuler-RISC-V org PR",1)
    wb.save(filepath)
    wb = load_workbook(filepath)
    ws = wb.worksheets[0]
    ws.column_dimensions["A"].width = 60
    ws.column_dimensions["B"].width = 60
    ws.append(header)
    for row in openEuler_PR:
        ws.append(row)
    max_row = ws.max_row
    max_column = ws.max_column
    side = Side(border_style='thin', color='FF000000')
    border = Border(left=side,right=side,top=side,bottom=side)
    for i in range(1, max_row+1):
        for j in range(1, max_column+1):
            ws.cell(i, j).border = border
    ws = wb.worksheets[1]
    ws.column_dimensions["A"].width = 60
    ws.column_dimensions["B"].width = 60
    ws.append(header)
    for row in openEulerriscv_PR:
        ws.append(row)
    max_row = ws.max_row
    max_column = ws.max_column
    for m in range(1, max_row+1):
        for n in range(1, max_column+1):
            ws.cell(m, n).border = border

    wb.save(filepath)

if __name__=="__main__":
    openEuler_PRdata = get_repoPRInfo(headers, token, openEulerrepo_url)
    repourllist = get_openEulerorg(headers, token)
    openEulerriscv_PRdata = get_openEulerriscvPRInfo(headers, token, repourllist)
    create_excel(filepath, openEuler_PRdata, openEulerriscv_PRdata, report_header)

    

