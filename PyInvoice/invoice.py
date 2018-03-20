import requests
import os
from bs4 import BeautifulSoup

os.system("title Penut PyInvoice")
page = requests.get("http://invoice.etax.nat.gov.tw/")
page.encoding = "UTF-8"
soup = BeautifulSoup(page.text, "html5lib")

title_text = soup.find_all("h2")
title1 = title_text[1].text
title2 = title_text[3].text
code_text = soup.find_all("span", {"class": "t18Red"})

codes = []

for c in code_text:
	cc = c.text.split("、")
	for ccc in cc:
		codes.append(ccc)

print(title1 + "\t" + title2)
for i in range(int(len(codes) / 2)):
	print(str(codes[i]).ljust(8) + "\t" + codes[i + 8])

month = input("\n請選擇月份：\n[1] %s\n[2] %s\n > " % (title1, title2))

if month == "1":
	codes = codes[:8]
else: codes = codes[8:]

print(codes)

while True:
	try:
		s = input("輸入發票末三碼：")
		flag = False
		for code in codes:
			if code[-3:] == s:
				print("Yeeeeeeeeeeeeee中啦")
				flag = True
		if not flag: print("未中獎")
	except:
		print(88888)
		break
