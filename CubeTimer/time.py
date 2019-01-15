import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def load_csTimer(data_path):
	ds = dict()
	with open(data_path, 'r', encoding='UTF-8') as fin:
		fin.readline()
		for line in fin:
			date, time = line.split(';')[-2:]
			date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
			if ds.get(date, None): print('err', date)
			ds[date] = float(time)
	return ds

def load_nanoTimer(data_path):
	ds = dict()
	with open(data_path, 'r', encoding='UTF-8') as fin:
		fin.readline()
		for line in fin:
			time, date = line.split(',')[2:4]
			date = datetime.strptime(date, '%b %d %Y - %H:%M:%S')
			if ds.get(date, None): print('err', date)
			ds[date] = float(time)
	return ds

def load_data(data_path):
	if 'csTimer' in data_path:
		return load_csTimer(data_path)
	else:
		return load_nanoTimer(data_path)

def drawMA(data, n):
	data4 = list()
	for i, _ in enumerate(data[:-n]):
		r = 0
		for ii in range(n):
			r += data3[i+ii]
		data4.append(r/n)
	plt.plot(data4)
	plt.savefig('ma%d.png' % n)
	plt.clf()


if __name__ == "__main__":
	data = dict()
	for dirPath, _, fileList in os.walk('./Records'):
		for fileName in fileList:
			fullPath = os.path.join(dirPath, fileName)
			data.update(load_data(fullPath))
	data2 = list()
	for k in data.keys():
		data2.append([k, data[k]])
	data2 = sorted(data2, key=lambda x: x[0])

	data3 = [d[1] for d in data2]
	plt.plot(data3)
	plt.savefig("avg.png")
	plt.clf()

	drawMA(data3, 3)
	drawMA(data3, 5)
	drawMA(data3, 10)
	drawMA(data3, 12)