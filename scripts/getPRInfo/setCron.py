from crontab import CronTab
import os

curDir=os.path.dirname(os.path.abspath(__file__))


cron=CronTab(user=True)
cmd="/usr/bin/python3.8 "+curDir+"/getPRInfo.py >> "+curDir+"/log.txt 2>&1 &"

job = cron.new(cmd)

job.setall("0 9 * * 3")
cron.write()
