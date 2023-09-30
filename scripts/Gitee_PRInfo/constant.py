import os

token = 'your gitee account token'


report_header = [
    'packageName',
    'rvPRUser',
    'rvPRUrl',
    'rvPRStatus',
    'created_at',
    'updated_at',
    'latest comment time',
    'latest comment submitter'
    ]
headers = {
    'Content-Type': 'application/json;charset=UTF-8'
    }
owner = 'openEuler-RISC-V'
excelfile = os.path.join(os.getcwd(), 'pr_info.xlsx')