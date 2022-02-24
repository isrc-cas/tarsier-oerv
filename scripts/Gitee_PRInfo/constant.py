import os

token = 'your gitee account token'


report_header = [
    'packageName',
    'rvPRUser',
    'rvPRUrl',
    'rvPRStatus',
    'created_at',
    'updated_at',
    'lastest comment time',
    'lastest comment submitter'
    ]
headers = {
    'Content-Type': 'application/json;charset=UTF-8'
    }
owner = 'openEuler-RISC-V'
excelfile = os.path.join(os.getcwd(), 'pr_info.xlsx')