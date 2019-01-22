# out_eng = open('e.txt', 'w', encoding='UTF-8')
# out_cht = open('c.txt', 'w', encoding='UTF-8')
# with open('cmn.txt', 'r', encoding='UTF-8') as fin:
#     for line in fin:
#         line = line.strip().split('\t')
#         out_eng.write(line[0] + '\n')
#         out_cht.write(line[1] + '\n')
# out_eng.close()
# out_cht.close()

eng = open('e.txt', 'r', encoding='UTF-8')
cht = open('a.txt', 'r', encoding='UTF-8')
out = open('cmn2.txt', 'w', encoding='UTF-8')

for line in cht:
    t = eng.readline().strip()
    out.write(t + '\t' + line)
    
out.close()
eng.close()
cht.close()