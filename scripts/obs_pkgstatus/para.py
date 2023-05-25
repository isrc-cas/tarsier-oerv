import os

obs_account = {'user': your username of obs account , 'password': your password of obs account}
obs_project = 'openEuler:23.03'
repolist = [{'arch': 'riscv64', 'repo': '23.02'}, {'arch': 'riscv64', 'repo': '23.03'}]
obs_url = 'https://build.tarsier-infra.com'

excelheader = ['package', 'revision'] + ['{} status'.format(repo['repo']) for repo in repolist]
excelfile = os.path.join(os.getcwd(), 'obs_pkginfo.xlsx')