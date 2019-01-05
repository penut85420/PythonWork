ct = open('./lexicon_ct.txt', 'r', encoding='utf-8')
cs = open('./lexicon_cs.txt', 'r', encoding='utf-8')
csct = open('./lexicon_csct.txt', 'w', encoding='utf-8')

for lcs in cs:
	lcs = lcs.strip()
	lct = ct.readline().strip()
	csct.write('%s\t%s\n' % (lcs, lct))

ct.close()
cs.close()
csct.close()