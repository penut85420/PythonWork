import sys
input()
ss = "[" + '"' + input() + '"'
for s in sys.stdin:
    if s.strip() == '': continue
    if s.startswith("G"): continue
    
    ss += ', "' + s[:-1] + '"'
ss += "]"
print(ss)
    
