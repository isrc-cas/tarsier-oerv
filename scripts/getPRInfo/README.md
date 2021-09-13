1. 将文件放至一个目录下，记为path（绝对路径）
2. 需要修改：config.ini中的dir为path
3. 将PR链接定义在watchlist.txt中
4. 修改setCron.py中command中的相关路径
5. 运行setCron.py
```
python3 setCron.py
crontab -l
```
可以看到配置的job<br>
目前定义的是每周三早上9点，可以根据需要修改
