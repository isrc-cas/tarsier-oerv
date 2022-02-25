import os

token = 'your gitee account token'
period = ['start_date', 'end_date']     # period = ['2022-02-01', '2022-02-24']



sheet1_header = [
    'packageName',
    'rvPRStatus',
    'rvPRUrl',
    'rvPRUser',
    'created_at'
    ]
sheet2_header = ['rvPRUser', 'number of PR']
report_header = [sheet1_header, sheet2_header]
headers = {
    'Content-Type': 'application/json;charset=UTF-8'
    }
owner = 'openEuler-RISC-V'
excelfile = os.path.join(os.getcwd(), 'pr_statistics.xlsx')