import PIL.Image
import PIL.ExifTags
import os
import subprocess

cmd = ['touch', '-d', '%s', '%s']

for dirPath, _, fileList in os.walk('./Photos/'):
	for fileName in fileList:
		try:
			p = os.path.join(dirPath, fileName)
			img = PIL.Image.open(p)
			exifdata = {
				PIL.ExifTags.TAGS[k]: v
				for k, v in img._getexif().items()
				if k in PIL.ExifTags.TAGS
			}
			_date = exifdata['DateTimeOriginal']
			_date, _time = _date.split(' ')
			_date = _date.replace(':', '')
			cmd[2] = '%s %s' % (_date, _time)
			cmd[3] = p
			subprocess.call(cmd)
			print(p, exifdata['DateTimeOriginal'])
		except: pass