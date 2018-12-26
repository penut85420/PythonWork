champ_list = open("champ_list.txt", 'r', encoding='UTF-8').read().split()

term_play = "用 玩 打".split()
term_of = "的 得".split()
term_adv = "真 有夠 非常 很 極 十分 極為 極度 極致 ".split()
term_good = "好 棒 讚 不錯 優秀 傑出 完美 漂亮 卓越 精彩 高超 了不起 優異 出色 精彩 出眾 出神入化 突出".split()
term_bad = "差勁 糟糕 不好 爛 不行 糟 差 不給力 拙劣 遜色 菜 差勁".split()
lines = 0
with open("desc_label.txt", 'w', encoding='UTF-8') as fout:
    for a in champ_list:
        for b in term_play:
            for c in term_of:
                for d in term_adv:
                    for e in term_good:
                        fout.write("%s %s %s %s %s\t%d\n" % (a, b, c, d, e, 1))
                        lines += 1
                        
                    for e in term_bad:
                        fout.write("%s %s %s %s %s\t%d\n" % (a, b, c, d, e, 0))
                        lines += 1
