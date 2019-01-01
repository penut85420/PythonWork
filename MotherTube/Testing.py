import pickle

import pytube
from pytube import Playlist, YouTube

url = r"https://www.youtube.com"

dlist = pickle.load(open('./dlist.pkl', 'rb'))
errlist = []
for d in dlist:
	try:
		yt = YouTube(url + d)
		print(url + d + ' ok')
	except Exception as e:
		print(url + d, e)
		errlist.append(d)

print(len(dlist), len(errlist))
