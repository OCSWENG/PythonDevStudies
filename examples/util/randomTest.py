import random

def func1():
	x = 1

def func2():
	x = 2

def func3():
	x = 3

def func4():
	x = 4

possible_funcs = [func1, func2, func3, func4]

statistics = {0 : 0, 1 : 0, 2 : 0, 3 : 0}
total = 1024

def getPercent(count):
	return (count/total)*100

for i in range (total):
	sel = random.randint(0,3)
	val = statistics[sel]
	val += 1
	statistics[sel]=val
	possible_funcs[sel]()

for k, v in statistics.items():
	print('Func{} : Hits={} Percentage={}'.format(k+1,v,getPercent(v)))

