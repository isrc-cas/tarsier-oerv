此脚本的目的是在obs上批量创建包，由于使用osc命令创建包需要权限（只有创建该project的人才有该权限）

所以此脚本目前只完成上传_service文件的功能，在此之前，如果目标project不是你创建的，需要将需要创建的包列表发送给project的创建者

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

osc上传_service
===
准备：
1. 如果需要,将包列表发送给有权限加包的人，请他帮忙在obs上创建包
2. 将packageList.txt,service_demo,updateServiceToObs.sh放到配置好osc环境的qemu中
3. osc环境中须有该project目录，如果没有请check out 目录, osc co <your project/your package>

命令：
bash updateServiceToObs.sh <your project>
