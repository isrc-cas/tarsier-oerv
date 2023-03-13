#### 脚本功能

下载obs指定工程中所有包的_service文件到本地

#### 使用方法

1. 执行 pip install -r requirements.txt 安装执行该脚本所需的python第三方库

2. 在 parameters.py 文件中设置以下参数

   ````
   obs_account = {'username':'your username of obs account', 'password':'your password of obs account'}
   obs_url = 'https://build.tarsier-infra.com'
   obs_project = 'openEuler:23.03'
   ````

   obs_account: obs账号的用户名和密码

   obs_url: obs url

   obs_project: 要下载_service文件的包所在的obs工程


3. 执行 python get_servicefile.py 运行脚本

   说明：get_servicefile.py中的2个函数：

   get_pkgs(url, account, project, filedir): 获取obs指定工程下所有包名，并存储到当前目录下 servicefile\packagelist.txt 文件中

   download_servicefile(url, account, project, firdir, packagelist): 下载指定工程中所有包的_service文件到当前目录下servicefile文件夹中的对应包名下，例如包名是adcli， _service就会下载到当前目录下 servicefile\adcli\ 路径下

   
