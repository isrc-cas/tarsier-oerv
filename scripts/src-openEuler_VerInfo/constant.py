import os
import time


token = your token of gitee account
obs_account = {'user':your username of obs account , 'password':your password of obs account}
branchlist = ['master', 'openEuler-22.03-LTS', 'openEuler-22.03-LTS-Next']
report_header = [
    'No.',
    'Package',
    'obs_repository',
    'obs_commit_id',
    'obs_status',
    'gitee_master',
    'gitee_openEuler-22.03-LTS',
    'gitee_openEuler-22.03-LTS-Next',
    'Lastest Update',
    'Upgrade Priority'
    ]


headers = {
    'Content-Type': 'application/json;charset=UTF-8'
    }
org = 'src-openEuler'
currenttime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
csvfile = os.path.join(os.getcwd(), 'pkgs_verinfo_{}.csv'.format(currenttime))
