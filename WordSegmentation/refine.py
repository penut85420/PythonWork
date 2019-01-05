import re

finn = open('./dictionary_main.txt', 'r', encoding='utf8')
fout = open('./lexicon_ct.txt', 'w', encoding='utf8')

r = re.compile("[\\+\\-\\(\\)!$%&;\\'\",\\.\\/\\*:：﹏－\\[\\]，、〜∼］［＝＜＞／a／～Ａ-Ｚ０-９＃！＠＃＄％︿＆＊（）—＋的ァ-ヿぁ-ゟㄱ-ㆎ가-힣ힰ-ퟻ ]+")
r2 = re.compile("([0-9A-Za-z]*)")
r3 = re.compile("[「𠀧𠄳𠊛𡦂𡨸𡨸𡨸𢀛𢀛𢀛𢀛𢄂𢆯𢆯𣍏𣘨𣛭𣝓𣝓𣬠𣶐𤩲𤭢𦀚𧈢𧉅𧊕𧐔𧑏𧑗𧒀𧒽𧒽𧴖𨁂𨦡𨦡𩫾𩷓𩽆𫃎𫙮𫚥𬲱󹿰]+")

for line in finn:
	if r.search(line): continue
	if r3.search(line): continue
	m = r2.search(line)
	if m and m.group(1) == line.strip(): continue
	fout.write(line)

finn.close()
fout.close()