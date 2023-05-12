import os

obs_account = {'user':your username of obs account , 'password':your password of obs account}
obs_project = 'openEuler:23.03'
repolist = ['23.02', '23.03']
obs_url = 'https://build.tarsier-infra.com'

excelheader = ['package', 'revision'] + ['{} status'.format(repo) for repo in repolist]
excelfile = os.path.join(os.getcwd(), 'obs_pkginfo.xlsx')