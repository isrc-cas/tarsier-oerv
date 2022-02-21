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
