import os

def getFileExt(s):
    for i, c in enumerate(reversed(s)):
        if c == '.': return s[-i:]
    return ""

targetDir = '/home/oppai/Downloads/Download/'

for dirPath, _, fileList in os.walk(targetDir):
    for fileName in fileList:
        old = os.path.join(dirPath, fileName)
        ext = getFileExt(old)
        new = fileName[:-len(ext)].title() + ext.lower()
        new = new.replace("Ai ", "AI ")
        new = new.replace("Nlp ", "NLP ")
        new = os.path.join(dirPath, new)
        os.rename(old, new)
        