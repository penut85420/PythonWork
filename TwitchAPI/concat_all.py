import os
import subprocess

for dirPath, _, fileList in os.walk('clips'):
    with open('in.txt', 'w', encoding='utf-8') as fout:
        for i in range(len(fileList)):
            fout.write("file '%s'" % os.path.join(dirPath, 'cut%d.mp4' % (i+1)) + '\n')
    
subprocess.call(['ffmpeg', '-f', 'concat', '-i', 'in.txt', '-c', 'copy', 'all.mp4'])