#### 脚本功能

删除obs指定工程中所有软件包或者指定工程中指定软件包

#### 使用方法

1.执行pip install -r requirements.txt安装执行该脚本所需的python第三方库

2.在parameters.py文件中设置以下参数

````
obs_account = {'username':'username of your obs account', 'password':'password of your obs account'}
obs_url = 'https://build.tarsier-infra.com'
````

obs_account: 设置obs账号的用户名和密码

obs_url: obs网址

3.在pkgs.txt文件中列出需要删除的软件包名，一行写一个软件包名，例如：

````
busybox
capstone
amtk
````

如果需要删除指定工程中的所有软件包，该步骤跳过

4.执行命令运行脚本

````
python del_pkg.py openEuler:23.03       //删除obs工程openEuler:23.03下的所有软件包
python del_pkg.py openEuler:23.03 pkgs.txt        //删除obs工程openEuler:23.03下的在pkgs.txt文件中列出的软件包
````