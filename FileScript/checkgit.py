import os
from os.path import join
import subprocess

for dirPath, dirList, fileList in os.walk('./'):
	if os.path.exists(join(dirPath, '.git')):
		print(join(dirPath, '.git'))
		p = join(dirPath, '.git')
		# subprocess.call(['git', '--git-dir=%s' % p, '--work-tree=%s' % dirPath, 'branch', '--set-upstream-to=origin/master', 'master'])
		subprocess.call(['git', '--git-dir=%s' % p, '--work-tree=%s' % dirPath, 'pull'])
