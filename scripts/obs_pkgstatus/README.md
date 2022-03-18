#### 脚本的功能
抓取obs指定工程中的所有软件包的revision，以及其在指定仓库下的构建结果，最终生成excel格式的report

#### 使用方法
1. 执行pip install -r requirements.txt安装执行该脚本所需的python第三方库

2. 在para.py文件中设置以下参数

   ````
   obs_account = {'user':your username of obs account , 'password':your password of obs account}
   obs_project = 'openEuler:Mainline:RISC-V'
   repolist = ['standard_riscv64', 'advanced_riscv64']
   ````

   obs_account 设置的是obs账号的用户名和密码

   obs_project 设置要抓取数据的obs工程

   repolist 设置要抓取数据的工程下的仓库

3. 执行python run.py运行脚本，会在脚本所在目录生成obs_pkginfo



