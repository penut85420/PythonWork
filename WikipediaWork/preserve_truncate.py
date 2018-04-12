import os
import re

pageBegin = "<page>"
pageEnd = "</page>"
titleBegin = "<title>"
titleEnd = "</title>"
inputDir = "zhwiki_main_tw"
outputDir = "zhwiki_preserve_tw//"
fileHead = "zhwikiPreserve_"
xmlHeader = '<?xml version="1.0" encoding="UTF-8"?>\n<pageset>\n'
preBegin = '<text xml:space="preserve">'
preEnd = "=="
baseFileSize = 4000000
fileNameFormat = "%s%s%.4d.xml"

os.makedirs(outputDir)
for dirPath, dirName, fileNames in os.walk(inputDir):
    fid = 1
    fout = open(fileNameFormat % (outputDir, fileHead, fid), "w", encoding="UTF-8")
    fout.write(xmlHeader)
    for fileName in fileNames:
        with open(dirPath + "\\" + fileName, "r", encoding="UTF-8") as fin:
            record = False
            for line in fin:
                if line.find(pageEnd) != -1:
                    fout.write("</preserve>\n")
                    record = False
                    if fout.tell() > baseFileSize:
                        fout.write("</pageset>\n")
                        print(fileNameFormat % (outputDir, fileHead, fid))
                        fid += 1
                        fout.close()
                        fout = open(fileNameFormat % (outputDir, fileHead, fid), "w", encoding="UTF-8")
                        fout.write(xmlHeader)
                elif line.find(preBegin) != -1:
                    fout.write(line.replace(preBegin, "<preserve>\n").strip() + "\n")
                    record = True
                elif line.find(preEnd) != -1:
                    record = False
                elif line.find(titleBegin) != -1:
                    fout.write(line.strip() + "\n")
                elif record: fout.write(line)

print("Preserve split done.")