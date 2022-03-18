import os

obs_account = {'user':your username of obs account , 'password':your password of obs account}
obs_project = 'openEuler:Mainline:RISC-V'
repolist = ['standard_riscv64', 'advanced_riscv64']



excelheader = ['package', 'revision'] + ['{} status'.format(repo) for repo in repolist]
excelfile = os.path.join(os.getcwd(), 'obs_pkginfo.xlsx')