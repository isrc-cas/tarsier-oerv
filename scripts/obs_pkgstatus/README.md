#### 脚本的功能
抓取obs指定工程中的所有软件包的revision，以及其在指定仓库下的构建结果，最终生成excel格式的report

#### 使用方法
1. 执行pip install -r requirements.txt安装执行该脚本所需的python第三方库

2. 在para.py文件中设置以下参数

   ````
   obs_account = {'user': your username of obs account , 'password': your password of obs account}
   obs_project = 'openEuler:23.03'
   repolist = [{'arch': 'riscv64', 'repo': '23.02'}, {'arch': 'riscv64', 'repo': '23.03'}]
   obs_url = 'https://build.tarsier-infra.com'
   ````

   obs_account 设置的是obs账号的用户名和密码

   obs_project 设置要抓取数据的obs工程

   repolist 设置要抓取数据的工程下的仓库以及其对应的架构

   obs_url 设置obs url

3. 执行python run.py运行脚本，会在脚本所在目录生成obs_pkginfo



