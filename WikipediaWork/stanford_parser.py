import importlib
from subprocess import Popen

ctcs = importlib.import_module("ctcs")

test_in = "StanfordParser\\test\\in.txt"
test_out = "StanfordParser\\test\\out.txt"

def parse_string(ss):
	s = ctcs.CtcsString(ss)

	with open(test_in, "w", encoding="UTF-8") as fout:
		fout.write(s.cs_str)

	p = Popen('what.bat')
	stdout, stderr = p.communicate()

	contents = ""
	with open(test_out, "r", encoding="UTF-8") as fin:
		for line in fin:
			contents += line
		return s.reduction(contents)

# print(parse_string("數學 是 利用 符號 語言 研究 數量 、 結構 、 變化 以及 空間 等 概念 的 一門 學科 ，\n\n從 某種 角度 看 屬於 形式科學 的 一 種 。"))