#### 脚本的功能
抓取openEuler中间仓[openEuler-RISC-V](https://gitee.com/openeuler-risc-v) PR信息，生成excel格式的report

#### 使用方法
1. 执行pip install -r requirements.txt安装执行该脚本所需的python第三方库
2. 将constant.py文件中的token = 'your gitee account token'中的'your gitee account token'换成使用者gitee账号对应的token(个人设置->私人令牌)
3. 执行python run.py运行脚本，会在脚本所在目录生成pr_info.xlsx



