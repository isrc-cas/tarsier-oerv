#### 脚本功能

读取pkg.txt文件里的包，disable这些包在obs指定工程下指定仓库的Build Flag

#### 使用方法

1. 执行 pip install -r requirements.txt 安装执行该脚本所需的python第三方库

2. 将需要disable Build Flag的包填入pkgs.txt, 例如：

   ````
   adcli
   ansible
   bcc
   clutter
   python-docker
   ````

2. 在 parameters.py 文件中设置以下参数

   ````
   obs_account = {'username':'your username of obs account', 'password':'your password of obs account'}
   obs_url = 'https://build.tarsier-infra.com'
   obs_project = 'openEuler:23.03'
   obs_repolist = ['23.02', '23.03']
   obs_post_data = {
       'repository': '', ##该项无需设置，后续执行时会导入obs_repolist中的repo
       'arch': 'All',
       'flag': 'build',
       'status': 'disable'
   }
   ````
   
   obs_account: obs账号的用户名和密码
   
   obs_url: obs url
   
   obs_project: 软件包所在的obs工程
   
   obs_repolist: 需要disable build flag的软件包所在的仓库列表。
   
   obs_post_data = {
       'repository': '',    ##该参数无需设置，后续在代码中会由obs_repolist导
       'arch': 'All',
       'flag': 'build',
       'status': 'disable'
   }
   
   这里需要说明的是测试脚本时发现repository设置为All时，虽然得到的response是成功的，但查看obs界面发现并没有成功，所以这里必须指定具体仓库名称。目前的解决方案是在执行代码时由obs_repolist导入仓库名称。

4. 执行 python set_pkg_tag.py 运行脚本

