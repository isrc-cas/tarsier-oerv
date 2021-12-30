脚本使用说明：

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



