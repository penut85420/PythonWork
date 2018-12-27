# -*- encoding: utf-8 -*-
import subprocess
import os

for dirPath, _, fileList in os.walk('./in/'):
	for filename in fileList:
		inn = dirPath + filename
		out = './out/' + filename + '.mp3'
		subprocess.call('ffmpeg -i "%s" -vn -acodec libmp3lame "%s"' % (inn.encode('utf8').decode('utf8'), out.encode('utf8').decode('utf8')))