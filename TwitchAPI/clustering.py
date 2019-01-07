with open('777.log', 'r', encoding='utf-8') as fin:
    pre = 0
    count = 0
    print(end='%9.3f\t[Group]\t' % pre)
    for line in fin:
        s, msg = line.split('\t')
        s = float(s)
        if s - pre > 30.0:
            print(count)
            print(end='%9.3f\t[Group]\t' % s)
            count = 0
        count += 1
        pre = s
        # print(end=line)

