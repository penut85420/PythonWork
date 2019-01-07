import subprocess

with open('777_group.log', 'r', encoding='utf-8') as fin:
    count = 1
    for line in fin:
        t, g, n = line.split('\t')
        try: n = int(n)
        except: n = 0
        if n > 10:
            t = float(t)
            print(t - 30.0)
            # ffmpeg -ss 1812 -t 30 -i 360257927.mp4 cut.mp4
            # ffmpeg -i 360257927.mp4 -ss 2080 -t 30 -an -c copy cut.mp4
            subprocess.call(['ffmpeg', '-i', '360257927.mp4', '-ss', str(t-30), '-t', '30', '-an', '-c', 'copy', 'clips/cut%d.mp4' % count])
            count += 1
