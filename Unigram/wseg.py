d, d_maxlen = dict(), 0
with open("lexicon_test.txt", 'r', encoding='utf-8') as fin:
    for line in fin:
        s = line.strip()
        d[s] = True
        if len(s) > d_maxlen:
            d_maxlen = len(s)

def wseg(strInn, strSeg, result):
    if len(strInn) == 0:
        result.append(strSeg.strip())
        return
    
    maxlen = seglen(strInn)
    while maxlen > 0:
        seg = strInn[:maxlen]
        if d.get(seg) != None:
            wseg(strInn[maxlen:], strSeg + " " + seg, result)
        maxlen -= 1
    return result

def seglen(s):
    i = d_maxlen
    if i > len(s): i = len(s)
    while d.get(s[:i]) == None and i > 1:
        i -= 1
    return len(s[:i])

fout = open("wseg_output.txt", 'w', encoding='utf-8')
fout.write('<?xml version="1.0" encoding="utf-8"?>\n')
fout.write('<TOPICSET>\n')
with open("wsegInput_test.txt", 'r', encoding='utf-8') as fin:
    for line in fin:
        fout.write('  <TOPIC>\n')
        sen = line.strip()
        fout.write('    <SENTENCE>' + sen + "</SENTENSE>\n")
        fout.write("    <SEGMENTATION>\n")
        id = 1
        for rr in wseg(sen, "", []):
            fout.write("      <SEGSEQ id=\"%d\">" % id + rr + "</SEGSEQ>\n")
            id += 1
        fout.write("    </SEGMENTATION>\n")
        fout.write('  </TOPIC>\n')
fout.write("</TOPICSET>\n")
fout.close()
