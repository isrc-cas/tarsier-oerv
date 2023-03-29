#### 脚本功能

下载obs指定工程中指定包在指定仓库中的log文件

#### 使用方法

1. 执行pip install -r requirements.txt安装执行该脚本所需的python第三方库

2. 在parameters.py文件中设置以下参数

   ````
   obs_account = {'username':'username of your obs account', 'password':'password of your obs account'}
   obs_url = 'https://build.tarsier-infra.com'
   obs_project = 'Mega:23.03'
   obs_buildinfo= {'repo': 'standard_aarch64', 'arch': 'aarch64'}
   obs_packagelist = ['annobin', 'busybox', 'cjose']
   ````

   obs_account: 设置obs账号的用户名和密码

   obs_url: obs网址

   obs_project: 要下载log的软件包所在的obs工程

   obs_buildinfo: 要下载log所在的仓库和架构

   obs_packagelist：要下载log的软件包名

3. 执行 python download_log.py 运行脚本

   脚本执行完成后，所下载的log会存储在当前脚本所在目录下的 logfile下的对应软件包目录下，例如下载gtk的log, 该log文件会被存储在脚本所在当前目录下的 logfile/gtk/中

   下载失败的软件包会被记录在当前脚本所在目录下的 logfile/download_failed_recorder.txt中

   