import MaximumMatch

csct = dict()

# print('CSCT mapping loading...')
with open('./lexicon_csct.txt', 'r', encoding='utf-8') as fin:
	for line in fin:
		cs, ct = line.strip().split('\t')
		csct[cs] = ct
# print('Done!')

# print('CS Segmentor loading...')
segt = MaximumMatch.Segmentor('./lexicon_cs.txt')
# print('Done!')

# s = "皇后在后面吃面"
# print('Segmenting')
# sseg = segt.seg(s)

# print("\n[Simplified Chinese]")
# print(sseg)

# sct = str()

# for seg in sseg.split():
# 	sct += csct.get(seg, seg)
# print("\n[Traditional Chinese]")
# print(sct)

# s = """欢庆麦克鸡块登台35周年！
# 为您呈现全球唯一黄金麦克鸡块！ ！ ！ ！
# 999纯金、造价破百万 (好闪！快戴上墨镜)
# 你，也有机会得到一块
# 快来参加麦克鸡块答题大挑战，累积答对6题，登录资料就有机会获得999纯金之「黄金麦克鸡块」乙块!""".replace('\n', ' ')
with open('./c.txt', 'r', encoding='UTF-8') as fin:
	for line in fin:
		s = line
		sseg = segt.seg(s)
		# print("\n[Simplified Chinese Seged]")
		# print(sseg)

		sct = str()

		for seg in sseg.split():
			sct += csct.get(seg, seg)
		# print("\n[Traditional Chinese]")
		print(sct)