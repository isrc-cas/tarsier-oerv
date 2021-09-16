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
  
  
4. 可能需要修改 setCron.py 中 cmd 中的 python 路径
  
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
