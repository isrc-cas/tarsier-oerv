from crontab import CronTab
cron=CronTab(user=True)

job = cron.new("/usr/bin/python3.8 /home/lazy/python/getPRInfo.py >> /home/lazy/python/log.txt 2>&1 &")
job.setall("0 9 * * 3")
cron.write()
