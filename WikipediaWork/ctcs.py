class CTCS:
    def __init__(self):
        self.ctcs = {}
        with open("data\\mapping_ctcs.txt", "r", encoding="UTF-8") as fin:
            try:
                for line in fin:
                    s = line.strip().split("\t")
                    if len(s) > 1 and s[0] != s[1]:
                        self.ctcs[s[0]] = s[1]
            except UnicodeDecodeError:
                pass
            except UnicodeEncodeError:
                pass
    
    def get_cs(self, s):
        result = ""
        for c in s:
            if self.ctcs.get(c) is not None:
                result += self.ctcs[c]
            else: result += c
        return result

    def __str__(self):
        return str(self.ctcs)

class CtcsString:
    ctcs = CTCS()
    def __init__(self, s):
        s = s.replace("\n", " ")
        self.org_str = s
        self.org_str_list = s.split(" ")
        self.cs_str = CtcsString.ctcs.get_cs(self.org_str)
        self.cs_str_list = self.cs_str.split(" ")
    
    def reduction(self, s):
        for i in range(len(self.cs_str_list)):
            s = s.replace(self.cs_str_list[i].strip(), self.org_str_list[i].strip())
        return s

    def __str__(self):
        return str(self.org_str_list) + str(self.cs_str_list)

    def __test__(self):
        ss = CtcsString("電影 是 一 種 表演藝術 、 視覺藝術 及 聽覺藝術 ，利用 膠卷 、 錄影帶 或 數位媒體 將 影像 和聲 音 捕捉 起來 ，再 加上 後期 的 編輯 工作 而 成 。")
        print(ss.cs_str())

c = CtcsString("視覺藝術")
s = "(NN 视觉艺术)"
print(c.cs_str)
print(c.reduction(s))
