#### 脚本使用说明

##### 1. 功能

这组脚本的功能是分别抓取obs和gitee上包的版本进行对比，并生成report。

##### 2. 使用方法

1)使用脚本之前需要先执行pip install -r requirements.txt一次性安装脚本中会使用到的python第三方库

2)使用前需要在constant.py文件中设置以下参数

````
token = your token of gitee account
obs_account = {'user':your username of obs account , 'password':your password of obs account}
````

token设置的是你的gitee账号的token, obs_account设置的是obs账号的用户名和密码

如果需要添加或者修改抓取的gitee分支，可以修改以下参数

````
branchlist = ['master', 'openEuler-22.03-LTS', 'openEuler-22.03-LTS-Next']
report_header = [
    'No.',
    'Package',
    'OBS_repository',
    'OBS_commit_id',
    'obs_status',
    'gitee_master',
    'gitee_openEuler-22.03-LTS',
    'gitee_openEuler-22.03-LTS-Next',
    'Lastest Update',
    'Upgrade Priority',
    'has rpm history',
    'rpm version'
    ]
````

branchlist里列出的是要抓取的gitee分支。

report_header里列出的是report中的各列的标题:

No. : 序号

Package: 包名

obs_repository: obs service文件中的gitee address

obs_commit_id: obs service文件中的gitee commit id

obs_status: obs中包的当前状态

gitee_master: 源码仓src-openeuler中master分支最新的commit id

gitee_openEuler-22.03-LTS: 源码仓src-openeuler中openEuler-22.03-LTS分支最新的commit id

gitee_openEuler-22.03-LTS-Next: 源码仓src-openeuler中openEuler-22.03-LTS-Next分支最新的commit id

Lastest Update: 在obs和源码仓src-openeuler的3个分支中时间最新的commit

has rpm history: 是否有曾经编译成功的rpm包

rpm version: 编译成功的源码包名

0：代表obs最新；

1：代表源码仓src-openeuler中master分支最新；

2：代表源码仓src-openeuler中openEuler-22.03-LTS分支最新；

3：代表源码仓src-openeuler中openEuler-22.03-LTS-Next分支最新；

Upgrade Priority: obs和源码仓src-openeuler的3个分支最新的不重复的commit id的个数

3)执行命令python run.py执行脚本抓取相关数据，并生成csv格式得report

