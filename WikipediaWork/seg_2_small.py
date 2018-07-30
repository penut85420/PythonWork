import os

dir_in = "zhwiki_sub_seg_fix\\"
dir_out = "zhwiki_sub_seg_fix_small\\"

threshold = 8
fid = 1

fout = open(dir_out + "zhwikiSeg%.4d.xml" % (fid), "w", encoding='UTF-8')
count = 0
fout.write("<pageset>")

for dirPath, dirNames, fileNames in os.walk(dir_in):    
    for fileName in fileNames:
        fin = open(dirPath + "\\" + fileName, "r", encoding='UTF-8')
        for line in fin:
            if (line.startswith("<pageset>")):
                continue
            if (line.startswith("</pageset>")):
                continue
            if (line.startswith("</category>")):
                count += 1
            
            fout.write(line)

            if (count >= threshold):
                fout.write("</pageset>")
                fout.close()
                fid += 1
                fout = open(dir_out + "zhwikiSeg%.4d.xml" % (fid), "w", encoding='UTF-8')
                count = 0
                fout.write("<pageset>")
