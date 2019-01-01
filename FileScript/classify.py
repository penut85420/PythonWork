# Classify files into yyyymm folder

import os
import datetime

parentDir = './Photos'
targetDir = './Photos'
if not os.path.exists(parentDir):
	os.mkdir(parentDir)
for dirPath, _, fileList in os.walk(targetDir):
    for filename in fileList:
        t = os.path.getmtime(dirPath + '/' + filename)
        t = datetime.datetime.fromtimestamp(t)
        tag = t.strftime("%Y%m")

        if not os.path.exists(os.path.join(parentDir, tag)):
            os.mkdir(os.path.join(parentDir, tag))

        os.rename(os.path.join(dirPath, filename), os.path.join(parentDir, tag, filename))
