# Fix the last modify date by file name

import os, re
import subprocess

r = re.compile("_(201.*?)_(.*)_?\.")
cmd = ['touch', '-d', '%s', '%s']

for dirPath, _, fileList in os.walk('./Photos/200212'):
	for fileName in fileList:
		print(fileName)
		m = r.search(fileName)
		if m:
			_date = m.group(1)
			_time = m.group(2)
			_time = "%s:%s:%s" % (_time[0:2], _time[2:4], _time[4:6])
			print(_date, _time)
			cmd[2] = '%s %s' % (_date, _time)
			cmd[3] = os.path.join(dirPath, fileName)
			subprocess.call(cmd)