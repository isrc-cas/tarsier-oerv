#### 脚本的功能
抓取指定时间段内openEuler中间仓[openEuler-RISC-V](https://gitee.com/openeuler-risc-v) PR信息，并根据提交人统计每个人在这段时间里提交pr的数量，生成excel格式的report

#### 使用方法
1. 执行pip install -r requirements.txt安装执行该脚本所需的python第三方库

2. 设置para.py文件

   1）token = 'your gitee account token'中的'your gitee account token'换成使用者gitee账号对应的token(个人设置->私人令牌)

   2）period = [‘start_date’, ‘end_date’]中设置要获取pr的时间段, start_date设置起始日期，end_date设置结束日期，输入的日期格式是：yyyy-mm-dd, 例如：period = ['2022-02-01', '2022-02-24']

3. 执行python run.py运行脚本，会在脚本所在目录生成pr_statistics.xlsx，excel文件会有2个sheet, 第一个sheet是指定时间内的pr信息，第二个sheet是这段时间里，每个提交人提交的pr数量



