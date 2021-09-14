1. 将文件放至一个目录下，记为 path （绝对路径）
2. 需要修改： config.ini 中的 dir 为 path
3. 将 PR 链接定义在 watchlist.txt 中
4. 修改 setCron.py 中 command 中的相关路径
5. 运行 setCron.py
```
python3 setCron.py
crontab -l
```
可以看到配置的 job

目前定义的是每周三早上9点，可以根据需要修改
