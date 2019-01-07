
with open('msg.log', 'r', encoding='utf8') as fin:
    for line in fin:
        if '777' in line:
            print(line, end='')