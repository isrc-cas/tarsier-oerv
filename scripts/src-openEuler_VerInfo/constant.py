import os
import time


token = 'your token of gitee account'
obs_account = {'user':your username of obs account , 'password':your password of obs account}
repolist = ['standard_riscv64', 'advanced_riscv64']
branchlist = ['master', 'openEuler-22.03-LTS', 'openEuler-22.03-LTS-Next']
report_header = [
    'No.',
    'Package',
    'obs repository',
    'obs commit id',
    'obs standard_riscv64 status',
    'obs advanced_riscv64 status',
    'gitee master',
    'gitee openEuler-22.03-LTS',
    'gitee openEuler-22.03-LTS-Next',
    'Latest Update',
    'Upgrade Priority',
    'has rpm history in standard_riscv64',
    'rpm version in standard_riscv64',
    'has rpm history in advanced_riscv64',
    'rpm version in advanced_riscv64'
    ]



headers = {
    'Content-Type': 'application/json;charset=UTF-8'
    }
org = 'src-openEuler'
currenttime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
csvfile = os.path.join(os.getcwd(), 'pkgs_verinfo_{}.csv'.format(currenttime))
