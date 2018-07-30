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
category = re.compile("\[\[Category:(.*?)[\|\]]")
category_cht = re.compile("\[\[分類:(.*?)[\|\]]")

for dirPath, dirName, fileNames in os.walk(inputDir):
    fid = 1
    fout = open(fileNameFormat % (outputDir, fileHead, fid), "w", encoding="UTF-8")
    fout.write(xmlHeader)
    for fileName in fileNames:
        with open(dirPath + "\\" + fileName, "r", encoding="UTF-8") as fin:
            record = False
            title_pass = False
            category_list = None
            for line in fin:
                if line.find(pageEnd) != -1:
                    if not title_pass:
                        fout.write("</preserve>\n")
                        record = False
                elif line.find(preBegin) != -1:
                    if not title_pass:
                        fout.write(line.replace(preBegin, "<preserve>\n").strip() + "\n")
                        record = True
                elif line.find(preEnd) != -1:
                    record = False
                elif line.find(titleBegin) != -1:
                    if category_list is not None and not title_pass:
                        fout.write("<category>\n")
                        for c in category_list:
                            fout.write(c + "\t") # TODO
                        fout.write("\n</category>\n")
                    category_list = None
                    if fout.tell() > baseFileSize:
                        fout.write("</pageset>\n")
                        print(fileNameFormat % (outputDir, fileHead, fid))
                        fid += 1
                        fout.close()
                        fout = open(fileNameFormat % (outputDir, fileHead, fid), "w", encoding="UTF-8")
                        fout.write(xmlHeader)

                    title = re.search("<title>(.*?)</title>", line).group(1)
                    if title is not None:
                        title_pass = re.search("(年表)|(列表)", title) is not None
                    else: title_pass = False
                    if not title_pass: fout.write(line.strip() + "\n")
                elif record and not title_pass:
                        fout.write(line)
                elif category.search(line) is not None:
                    if category_list is None: category_list = []
                    category_list.append(category.search(line).group(1))
                elif category_cht.search(line) is not None:
                    if category_list is None: category_list = []
                    category_list.append(category_cht.search(line).group(1))


print("Preserve split done.")
