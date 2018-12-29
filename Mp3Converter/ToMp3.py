# -*- encoding: utf-8 -*-
import subprocess
import os

arg = list()
arg.append('ffmpeg')
arg.append('-i')
arg.append('%s')
arg.append('-vn')
arg.append('-acodec')
arg.append('libmp3lame')
arg.append('%s')

for dirPath, _, fileList in os.walk('./in/'):
	for filename in fileList:
		inn = os.path.join(dirPath, filename)
		out = os.path.join('./out/', filename + '.mp3')
		arg[2] = '%s' % inn
		arg[6] = '%s' % out
		subprocess.call(arg)