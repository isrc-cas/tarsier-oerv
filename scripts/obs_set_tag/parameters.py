obs_account = {'username':'your username of obs account', 'password':'your password of obs account'}
obs_url = 'https://build.tarsier-infra.com'
obs_project = 'openEuler:23.03'
obs_repolist = ['23.02', '23.03']
obs_post_data = {
    'repository': '',    ## 该项无需设置，后续执行时会导入obs_repolist中的repo
    'arch': 'All',
    'flag': 'build',
    'status': 'disable'
}