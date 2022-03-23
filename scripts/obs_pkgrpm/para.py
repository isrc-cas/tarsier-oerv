import os

obs_account = {'user':your username of obs account , 'password':your password of obs account}
obs_project = 'home:xijing:branches:openEuler:22.03:LTS:Next'
repolist = ['riscv64_stage1']



excelheader = ['package']
for repo in repolist:
    excelheader.extend(['has rpm history in {}'.format(repo), 'rpm version in {}'.format(repo)])

excelfile = os.path.join(os.getcwd(), 'obs_rpminfo.xlsx')
