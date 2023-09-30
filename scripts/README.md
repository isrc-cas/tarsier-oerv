[./addPackageToOBS/README.md](./addPackageToOBS/README.md)
此脚本的目的是在obs上批量创建包

脚本使用步骤如下

安装依赖
===
pip install -r ./requirements.txt

获取包列表
===
准备：
1. 修改config.ini中的target_package，此为搜索src源码仓的关键字
2. 修改config.ini中的gitee_cookie为你的cookie

命令：
python3 searchPackageFromSrc.py

运行完此命令后包会列在当前路径下的gitee_PackageList_%(target_package)s.xlsx文件中

判断是否需要获取commit ID
===
此步骤的目的是判断是否需要获取commit id，如果需要获取所有包的commit id则不需要执行此步骤，如果需要新增包，则执行此步骤，该脚本会为obs工程中没有的包打上标记

准备：
1. 修改config.ini中的obs_cookie为你的OBS cookie
2. 修改config.ini中的obs_domain，oerv obs 或者 oe obs
3. 修改config.ini中的project为需要查询的工程，例如Factory:RISC-V:Python
4. 如果不使用步骤1中生成的表格，则需要配置config.ini中的record_file和sheetname

命令：
python3 checkObsHasPackage.py

运行完此脚本，会在表格中加一列needCommitId

获取最新的commit id
===
此步骤会根据needCommitId列判断是否需要获取commit id，如果没有该列，则获取所有包的commit id
准备：
1. 修改config.ini中的gitee_token为你的gitee token
2. 修改config.ini中的branch为需要获取最新commit id的分支，当该分支不存在时，脚本会获取master分支的commit id
3. 如果不使用步骤1中生成的表格，则需要配置config.ini中的record_file和sheetname

命令：
python3 getLatestCommit.py

运行完此脚本，会在表格中加一列commit id

筛选需要的包和commit id
===
此步骤需要手动，在表格中筛选需要的包和commit id，存放在packageList.txt中
![image](https://user-images.githubusercontent.com/89906695/167054328-03f7e409-21c9-4409-bb99-d8f03dff08d3.png)

osc创建包并上传_service文件
===
准备：
1. 将packageList.txt,service_demo,addPackageToObs.sh放到配置好osc环境的qemu中
2. osc环境中须有该project目录，如果没有请check out 目录, osc co <your project/your package>

命令：
bash addPackageToObs.sh \<your project\>
[./dependent_package/README.md](./dependent_package/README.md)
##### 1. 实现功能

该自动化脚本实现的功能输入需要查询的包，生成与所输入包存在依赖和被依赖关系的所有包的关系图

##### 2. 文档说明

getspec.py  执行该文件可获取openEuler-riscv的所有包的spec，获取到的spec存放在specfile.json中

specfile.json  存放openEuler-riscv的所有包的spec信息

getbuildrequires.py 执行改文件可根据spec文件获取所有包的依赖包，获得的依赖包存放在buildrequiresfile.json中
getbuildrequires-xls.py将包以及其依赖关系写入到../../data/dep_info.xlsx中

buildrequiresfile.json 存放所有包的依赖包的信息

inputfile.json 提供给用户输入需要查询的包，可输入多个

run.py 执行该文件可生成所要查询包的（inputfile.json里输入的包）相关依赖和被依赖包的关系图（pdf文档）

graph-output 生成的关系图存放在该文件夹中

requirements.txt 执行该文件夹中的py档需要安装的python第三方库

getobs.py 执行该文件会抓取https://build.openeuler.org/project/monitor/openEuler:Mainline:RISC-V 界面的unresolvable和succeeded状态的包,并将获得这些包存放在packagelist.json中

packagelist.json 存放getobs.py中获取的unresolvable和succeeded状态的包

getfailrequires.py 生成packagelist.xlsx report

packagelist.xlsx 第一个sheet内容是https://build.openeuler.org/project/monitor/openEuler:Mainline:RISC-V 界面succeeded状态的包；第二个sheet内容是unresolvable状态的包的所有依赖包；将所有unresolvable状态的包的依赖包和所有succeeded状态的包的依赖包用自动化做了对比(没有去掉-dev，pkgconfig等后缀)，这样对比出来的没有在succeeded中的依赖包存放在第三个sheet

##### 3. 使用方法

在inputfile.json中写入要查询的包，保存，然后执行run.py文件，就可以生成包的依赖关系图了。这里需要注意：

1）在inputfile.json中写入要查询的包，可一次输入多个。建议一次不要输入太多包，否则生成的图在显示一张图上可能会模糊不清

2）由于查询所使用的buildrequiresfile.json中存储的包名分别是spec文件中的Name和BuildRequires栏位的包名，所以写入需要查询的包名必须要与spec文件中的Name和BuildRequires栏位的包名保持一致，否则会查询不到

3）运行前需要安装requirements.txt里python第三方库，执行pip install -r requirements.txt可一次性安装，另外由于依赖关系图是由graphviz生成的，所以还需要安装graphviz程序，graphviz安装程序下载地址http://www.graphviz.org/download/

4）将constant.py文件中的'your gitee account token'换成使用者gitee账号对应的token(个人设置->私人令牌)


##### data/compare下的表格生成
1. 当obs上的包总数发生变化、依赖关系发生变化：
    1）getspec.py
    2）getbuildrequires-xls.py
2. 当obs构建状态发生变化：
    3）getObsInfo2xlsx.py
3. compare下的表格，基于obs数据和依赖数据在excle中整理和统计




[./download_fedora_riscv_rpm/README.md](./download_fedora_riscv_rpm/README.md)
#### 脚本使用说明

##### 1. 功能

这组脚本的功能是根据文件java_pkgs.txt中列出的包名，到http://fedora.riscv.rocks/koji/上去找到其已经构建成功的rpm包(不包括src)，将其下载下来，并生成每一个包是否下载成功的excel格式的report

##### 2. 文档说明

java_pkgs.txt：需要在http://fedora.riscv.rocks/koji/上查找并下载rpm包的包名

requirements.txt：执行该文件夹中的py档需要安装的python第三方库

para.py：变量文件，存储脚本中需要使用到的变量

get_package.py：获取java_pkgs.txt中列出的包在http://fedora.riscv.rocks/koji/中的buildID

pkgs_info.json：存储get_package.py执行后得到的结果

get_rpmlist.py：根据buildID获取java_pkgs.txt中列出的包对应的rpm list(不包括src)

rpm_info.json：存储get_rpmlist.py执行后得到的结果

download.py：从文件rpm_info.json中读取数据，下载rpm包，下载的rpm会存储在当前目录下的downloaded_rpm文件夹下，下载结束后在当前目录下生成文件名是pkgs_rpm_result.xlsx的report

pkgs_rpm_result.xlsx：存储rpm包下载是否成功的report，report中RPM Name栏位显示none，就表示在http://fedora.riscv.rocks/koji/没有找到相应的rpm包

##### 3. 使用方法

##### 3.1 安装python第三方库

在使用脚本之前需要先执行pip install -r requirements.txt一次性安装脚本中会使用到的python第三方库，在安装koji时若遇到错误，造成无法安装，可以执行下面的命令：

sudo apt -y install gcc libkrb5-dev
sudo apt -y install python3-dev

然后再次安装koji

###### 3.2 执行脚本获取数据

1）执行get_package.py，获取java_pkgs.txt中列出的包在http://fedora.riscv.rocks/koji/中的buildID

2）执行get_rpmlist.py，获取包对应的rpm list(不包括src)

3）执行download.py，下载rpm包，并生成report。下载的包会存放在脚本所在目录下的downloaded_rpm文件夹下，生成的report会存放在脚本所在目录下



[./getPRInfo/README.md](./getPRInfo/README.md)
1. 将文件放至一个目录下

2. 使用以下命令安装依赖包
```
pip3 install -r requirements.txt
```

3. 需要修改： config.ini.template
* token 处填写你的私人令牌，不需要引号
* 可以替换 orgs 和 repo 为你需要的组织或仓库，目前只支持一个组织和一个仓库，如果将来需要支持多个，再更新代码
* ignoreComment 为需要忽略的评论的人名，目前是我发现的机器人，如果将来发现其他可以追加在后面，以","分割<br>

  修改完以后将 config.ini.template 重命名为 config.ini
  
  
4. 可能需要修改 setCron.py 中 cmd 中的 python 相关路径为你的python路径
  
5. 运行 setCron.py, 然后可以看到当前生效的 job
```
python3 setCron.py
crontab -l
```

目前定义的是每周三早上9点，可以根据需要修改
如果需要删除 job ，可以使用以下命令
```
crontab -r
```
* 由于使用了python-crontab库，整套脚本需要在Linux环境下运行
[./GiteePRTracker/README.md](./GiteePRTracker/README.md)
# Gitee PR Tracker

## 安装依赖及配置

`pip3 install -r requirements.txt `

运行前需要先在 `config.ini` 中配置 Gitee Cookie 和 Token，程序运行最开始会检测是否可以成功登录。

因为采用爬虫方式获取数据，Gitee 目前不允许未登录用户搜索 PR，所以需要可以成功登录的 Cookie。

可以在不设置 Token 的情况下使用，但 Gitee 的 API 限制较为严格，所以建议使用 Token。

Token 和 Cookie 字符串不需要使用引号包裹。

## 使用

`python main.py [开始时间] [结束时间] [用户名...]`

或者在 `usernames.txt` 的中配置用户名，每行一个用户，然后运行 `python main.py [开始时间] [结束时间]`。

如果 `usernames.txt` 中有用户名的配置则优先使用 `usernames.txt` 中的配置，否则使用命令行参数。

## 样例

`python3 main.py 2022-08-01 2022-08-20 lvxiaoqian misaka00251 Jingwiw jchzhou`

终端中会以 ASCII 表格的方式生成预览

![](screenshot.png)

文件夹下会生成以执行时间为名的 `csv` 文件，使用任何表格处理软件打开即可。

![](csv.png)[./GiteePR_statistics/README.md](./GiteePR_statistics/README.md)
#### 脚本的功能
抓取指定时间段内openEuler中间仓[openEuler-RISC-V](https://gitee.com/openeuler-risc-v) PR信息，并根据提交人统计每个人在这段时间里提交pr的数量，生成excel格式的report

#### 使用方法
1. 执行pip install -r requirements.txt安装执行该脚本所需的python第三方库

2. 设置para.py文件

   1）token = 'your gitee account token'中的'your gitee account token'换成使用者gitee账号对应的token(个人设置->私人令牌)

   2）period = [‘start_date’, ‘end_date’]中设置要获取pr的时间段, start_date设置起始日期，end_date设置结束日期，输入的日期格式是：yyyy-mm-dd, 例如：period = ['2022-02-01', '2022-02-24']

3. 执行python run.py运行脚本，会在脚本所在目录生成pr_statistics.xlsx，excel文件会有2个sheet, 第一个sheet是指定时间内的pr信息，第二个sheet是这段时间里，每个提交人提交的pr数量



[./Gitee_PRInfo/README.md](./Gitee_PRInfo/README.md)
#### 脚本的功能
抓取openEuler中间仓[openEuler-RISC-V](https://gitee.com/openeuler-risc-v) PR信息，生成excel格式的report

#### 使用方法
1. 执行pip install -r requirements.txt安装执行该脚本所需的python第三方库
2. 将constant.py文件中的token = 'your gitee account token'中的'your gitee account token'换成使用者gitee账号对应的token(个人设置->私人令牌)
3. 执行python run.py运行脚本，会在脚本所在目录生成pr_info.xlsx



[./OBSProjStats/README.md](./OBSProjStats/README.md)
#### 功能 
抓取 obs 中指定的 project repo 的所有软件包的revision，以及其在指定仓库下的构建结果，生成 csv
crawl every package status for every arch in specific repo & project. 
不需要登陆 OBS , 理论上也适用于其他 OBS.
no need to login.

#### 使用方法
1.  执行pip install -r requirements.txt安装执行该脚本所需的python第三方库
2.  在para.py文件中设置以下参数
 
    ```py
    csvName = "<filename>.csv"
    projRepoUrl = {
    "openEuler_2209": "https://build.tarsier-infra.com/project/monitor/openEuler:22.09",  # example
    "<repoName>": "<ProjectMonitorUrl>"
    ```
    <repoName> 是 project monitor 页面上 Repository 里的选项

    <ProjectMonitorUrl> 是 project 里 monitor 选项卡的 url
    
3. 执行python main.py运行脚本，会在脚本所在目录生成 csvName 里指定名称的 csv 文件。可导入 Excel 进行分析统计。


#### TODO 
 - 通过仓库的 _service 文件获取工程下该软件包所指定的 commit 
 - 导出其他格式如 markdown table (引入 pandas 库)
 -  
[./OBSVersionTracker/README.md](./OBSVersionTracker/README.md)
# OBS Version Tracker

## 安装依赖及配置

`pip3 install -r requirements.txt `

运行前需要先在 `config.ini` 中配置 OBS 的地址、用户名、密码。程序运行最开始会检测是否可以成功登录。

## 使用

在 `project.ini` 中配置需要抓取的工程，为每个工程新建一个 Section，使用 `[]` 包裹，可以同时配置多个工程。

在这个 Section 中，需要配置 arch 和 repo 两个参数，分别表示工程的架构和需要抓取的仓库。

arch 字段必须配置，repo 字段可以不配置，不配置时默认抓取所有仓库。

当需要抓取指定多个仓库时，repo 字段可以加入多个参数，使用逗号分隔。

运行 `python main.py` 开始抓取数据，在数据采集完成后，会在当前目录下创建以程序运行时间命名的文件夹，抓取的数据会保存在这个文件夹中。

每个仓库的数据会保存在一个单独的文件中，文件名为 `工程名:仓库名.csv`。

## 样例

```ini
[Factory:RISC-V]
arch = riscv64
repo = 22.09, Roll
```
这段配置会抓取 Factory:RISC-V 工程中的 22.09 和 Roll 仓库的数据。

```ini
[Factory:RISC-V:Rust]
arch = riscv64
repo =
```
这段配置会抓取 Factory:RISC-V:Rust 工程中的所有仓库的数据。

## 运行结果

![](screenshot.png)

终端中会显示抓取的进度，抓取完成后会显示抓取的数据量，包含仓库中的包数量、成功的包数量、失败的包数量。

其中，失败的包为无法抓取到构建时版本号的包。

![](csv.png)

csv 样例如上。

[./obs_pkgrpm/README.md](./obs_pkgrpm/README.md)
#### 脚本的功能
抓取obs指定工程中所有软件包在指定仓库下是否有编译成功的rpm包，如果有就列出源码包名，最终生成excel格式的report

#### 使用方法
1. 执行pip install -r requirements.txt安装执行该脚本所需的python第三方库

2. 在para.py文件中设置以下参数

   ````
   obs_account = {'user':your username of obs account , 'password':your password of obs account}
   obs_project = 'home:xijing:branches:openEuler:22.03:LTS:Next'
   repolist = ['riscv64_stage1']
   ````

   obs_account 设置的是obs账号的用户名和密码

   obs_project 设置要抓取数据的obs工程

   repolist 设置要抓取数据的工程下的仓库

3. 执行python run.py运行脚本，会在脚本所在目录生成obs_rpminfo.xlsx



[./obs_pkgstatus/README.md](./obs_pkgstatus/README.md)
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



[./recordHasRPM/README.md](./recordHasRPM/README.md)
本脚本可以实现两个功能

1. 通过project和repo获取有关包是否已经有成功构建的rpm

2. 读取excel第一列包名，在最后一列加上在相应project和repo下是否有成功构建的rpm


python3 recordHasRPM.py
--
该命令可以搜索某关键字包在某个project下某个repo下是否有成功生成的rpm

需在config.ini中修改：

project

repo

target_package（为空则搜索project下所有包）

cookie

python3 recordHasRPMFromExcel.py
--
该命令可以查询excel中某sheet第一列中包是否有构建成功的rpm

需在config.ini中修改：

project

repo

filename（excel文件名称）

sheetname

beginrow（包名开始的行）

cookie
[./resize-rootfs/README.md](./resize-rootfs/README.md)
此目录下的内容用于给D1添加第一次起动时自动扩展rootfs，只需要把resize-rootfs.tar.gz解压到镜像的根目录
[./src-openEuler_VerInfo/README.md](./src-openEuler_VerInfo/README.md)
#### 脚本使用说明

##### 1. 功能

这组脚本的功能是分别抓取obs和gitee上包的版本进行对比，并生成report。

##### 2. 使用方法

1)使用脚本之前需要先执行pip install -r requirements.txt一次性安装脚本中会使用到的python第三方库

2)使用前需要在constant.py文件中设置以下参数

````
token = 'your token of gitee account'
obs_account = {'user':your username of obs account , 'password':your password of obs account}
````

token设置的是你的gitee账号的token, obs_account设置的是obs账号的用户名和密码

如果需要添加或者修改抓取的gitee分支，可以修改以下参数

````
branchlist = ['master', 'openEuler-22.03-LTS', 'openEuler-22.03-LTS-Next']
report_header = [
    'No.',
    'Package',
    'obs repository',
    'obs commit id',
    'obs standard_riscv64 status',
    'obs advanced_riscv64 status',
    'gitee master',
    'gitee openEuler-22.03-LTS',
    'gitee openEuler-22.03-LTS-Next',
    'Latest Update',
    'Upgrade Priority',
    'has rpm history in standard_riscv64',
    'rpm version in standard_riscv64',
    'has rpm history in advanced_riscv64',
    'rpm version in advanced_riscv64'
    ]
````

branchlist里列出的是要抓取的gitee分支。

report_header里列出的是report中的各列的标题:

No. : 序号

Package: 包名

obs repository: obs service文件中的gitee address

obs commit id: obs service文件中的gitee commit id

obs standard_riscv64 status: obs中包在standard_riscv64库里的当前状态

obs advanced_riscv64 status: obs中包在advanced_riscv64库里的当前状态

gitee master: 源码仓src-openeuler中master分支最新的commit id

gitee openEuler-22.03-LTS: 源码仓src-openeuler中openEuler-22.03-LTS分支最新的commit id

gitee openEuler-22.03-LTS-Next: 源码仓src-openeuler中openEuler-22.03-LTS-Next分支最新的commit id

Latest Update: 在obs和源码仓src-openeuler的3个分支中时间最新的commit

has rpm history in standard_riscv64: 在standard_riscv64库里是否有曾经编译成功的rpm包

rpm version in standard_riscv64: 在standard_riscv64库里编译成功的源码包名

has rpm history in advanced_riscv64: 在advanced_riscv64库里是否有曾经编译成功的rpm包

rpm version in advanced_riscv64: 在advanced_riscv64库里编译成功的源码包名

0：代表obs最新；

1：代表源码仓src-openeuler中master分支最新；

2：代表源码仓src-openeuler中openEuler-22.03-LTS分支最新；

3：代表源码仓src-openeuler中openEuler-22.03-LTS-Next分支最新；

Upgrade Priority: obs和源码仓src-openeuler的3个分支最新的不重复的commit id的个数

3)执行命令python run.py执行脚本抓取相关数据，并生成csv格式得report

