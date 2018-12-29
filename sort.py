import os
import datetime

def getFileExt(s):
    for i, c in enumerate(reversed(s)):
        if c == '.': return s[-i:]
    return ""

targetDir = './Downloads'
destDir = './Downloads'
d = dict()

for dirPath, _, fileList in os.walk(targetDir):
    for fileName in fileList:
        t = os.path.getmtime(os.path.join(dirPath, fileName))
        t = datetime.datetime.fromtimestamp(t)
        e = getFileExt(fileName)
        n = t.strftime("%Y%m%d-%H%M%S." + e)
        os.rename(os.path.join(dirPath, fileName), os.path.join(destDir, n))