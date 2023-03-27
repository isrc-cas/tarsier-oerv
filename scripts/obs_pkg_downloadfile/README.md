#### 脚本功能

下载obs指定工程中所有包的_service或者spec文件到本地

#### 使用方法

1. 执行 pip install -r requirements.txt 安装执行该脚本所需的python第三方库

2. 在 parameters.py 文件中设置以下参数

   ````
   obs_account = {'username':'your username of obs account', 'password':'your password of obs account'}
   obs_url = 'https://build.tarsier-infra.com'
   obs_project = 'openEuler:23.03'
   
   #文件类型设置
   filetype='service'  ##下载spec文件时，此处设置为spec;下载service文件时，此处设置为service
   ````
   
   obs_account: obs账号的用户名和密码
   
   obs_url: obs url
   
   obs_project: 要下载_service文件的包所在的obs工程
   
   filetype: 要下载的文件类型，目前支持两种service和spec, 分别对应obs上软件包中的_service文件和spec文件


3. 执行 python download_file.py 运行脚本

   当下载service文件时，会
   获取obs指定工程下所有包名，并存储到当前目录下 servicefile\packagelist.txt 文件中;
   下载指定工程中所有包的_service文件到当前目录下servicefile文件夹中的对应包名下，例如包名是adcli， _service就会下载到当前目录下 servicefile\adcli\ 路径下;
   _service文件下载失败的软件包会被记录到当前目录下 servicefile\download_failed_recorder.txt 文件中

   当下载spec文件时，会
   获取obs指定工程下所有包名，并存储到当前目录下 specfile\packagelist.txt 文件中；
   下载指定工程中所有包的spec文件到当前目录下specfile文件夹中的对应包名下，例如包名是adcli，spec文件就会下载到当前目录下 specfile\adcli\ 路径下；
   spec文件下载失败的软件包会被记录到当前目录下 specfile\download_failed_recorder.txt 文件中

   
