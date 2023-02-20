#### 脚本功能

执行obs指定工程中指定包Trigger Rebuild功能

#### 使用方法

1. 执行pip install -r requirements.txt安装执行该脚本所需的python第三方库

2. 在parameters.py文件中设置以下参数

   ````
   obs_account = {'username':'username of your obs account', 'password':'password of your obs account'}
   obs_url = 'https://build.tarsier-infra.com'
   obs_project = 'openEuler:23.03'
   obs_packagelist = ['adcli', 'python-docker']
   ````

   obs_account: 设置obs账号的用户名和密码

   obs_url: obs网址

   obs_project: 要执行Trigger Rebuild的包所在的obs工程

   obs_packagelist: 要执行Trigger Rebuild的包列表

3. 执行python pkg_rebuild.py运行脚本