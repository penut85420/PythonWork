import os

folder_in = "zhwiki_sub_seg"
folder_out = "zhwiki_sub_seg_fix"

for dirPath, dirNames, fileNames in os.walk(folder_in):
    for fileName in fileNames:
        fin = open(dirPath + "\\" + fileName, "r", encoding="UTF-8")
        fout = open(folder_out + "\\" + fileName, "w", encoding="UTF-8")
        for line in fin:
            if line.startswith("<title>"):
                fout.write("<page>\n")
                fout.write(line)
            elif line.startswith("</preserve>"):
                fout.write(line)
                fout.write("</page>\n")
            else: fout.write(line)
        fin.close()
        fout.close()
