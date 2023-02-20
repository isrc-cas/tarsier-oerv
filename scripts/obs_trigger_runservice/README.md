#### 脚本功能

触发obs指定工程中所有软件包的更新或者指定工程中指定软件包的更新

#### 使用方法

1. 执行pip install -r requirements.txt安装执行该脚本所需的python第三方库

2. 在parameters.py文件中设置以下参数

   ````
   obs_account = {'username':'username of your obs account', 'password':'password of your obs account'}
   obs_url = 'https://build.tarsier-infra.com'
   gitee_token = 'your gitee token'
   ````
   
   obs_account: 设置obs账号的用户名和密码
   
   obs_url: obs网址
   
   gitee_token: gitee账号的私人令牌
   
3. 执行命令运行脚本

   ````
   python trigger_obs.py openEuler:23.03       //更新obs工程openEuler:23.03下的所有软件包
   python trigger_obs.py openEuler:23.03 A-Tune        //更新obs工程openEuler:23.03下的软件包A-Tune
   ````