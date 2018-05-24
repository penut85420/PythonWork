class lexTreeNode:
    def __init__(self, s):
        s = s[1:-1] # Remove ()
        self.txt = ""
        if s.find("(") != -1:
            self.tag = s[:s.find("(")].strip()
        else:
            self.tag = s[:s.find(" ")]
            self.txt = s[s.find(" ") + 1:]
        self.child = []
        s = s[s.find("("):]
        left = 0
        leftIdx = 0
        flag = False
        for i in range(len(s)):
            if (s[i] == "("): 
                left += 1
                flag = True
            elif (s[i] == ")"): 
                left -= 1

            if left == 0 and flag:
                self.child.append(lexTreeNode(s[leftIdx:i+1].strip()))
                leftIdx = i + 1
                flag = False

    def __str__(self):
        s = self.tag
        if self.txt != "":
            s += " [" + self.txt + "] "
        if len(self.child) > 0: s += " {"
        for child in self.child:
            s += str(child) + " "
        if len(self.child) > 0: s += "}"
        return s

    def get_npnn(self):
        result = []
        if self.tag == "NP":
            for child in self.child:
                if child.tag == "NN":
                    result.append(child.txt)
                elif child.tag == "NP":
                    child_nn = child.get_npnn()
                    for nn in child_nn:
                        result.append(nn)
        return result

    def find_title_is(self, title):
        found_title = False
        for c in self.child:
            npnn = c.get_npnn()
            if not found_title and len(npnn) == 1 and npnn[0] == title:
                found_title = True
                continue
            elif found_title and c.tag == "VP":
                return c.child[-1].get_npnn()

        for child in self.child:
            result = child.find_title_is(title)
            if result != None:
                return result
        return None
    
    def test(self):
        for c in self.child:
            if c.tag == "NP":
                print(self.tag + str(c.get_npnn()))
            c.test()

def main():
    fin = open("test_fin/a.lex", "r", encoding="UTF-8")
    contents = ""
    for line in fin:
        contents += line.strip()

    tree = lexTreeNode(contents)
    print(tree.find_title_is("數學"))

main()