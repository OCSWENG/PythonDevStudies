import time
from functools import wraps

import matplotlib.pyplot as plt
import numpy as np


times  = []

def timethis (func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.clock()
		r = func(*args, **kwargs)
		end = time.clock()
		print ('{}.{}:{}'.format(func.__module__, func.__name__, end-start))
                times.append(end-start)
		return r
	return wrapper

@timethis
def string_concat  (num_items):
	word = "" 
	nums = ""
	for n in range (num_items):
		nums += str(n)
	word = nums

@timethis
def append_and_join (num_items):
	word = "" 
	nums = []
	for n in range (num_items):
		nums.append(str(n))
	word = "".join(nums)

@timethis
def list_comprehension_and_join (num_items):
	word = "" 
	nums = [str(n) for n in range(num_items)]
	word =  "".join(nums)

@timethis
def generator_join (num_items):
	word = ""
	nums = (str(n) for n in range(num_items))
	word = "".join(nums)


# Obtain times
times1 = [0.0]
times2 = [0.0]
times3 = [0.0]
times4 = [0.0]

num_attempts = 6
scale =10
num_items = 650

for itr2 in range (0,num_attempts):
	print "NUM ITEMS {}".format(num_items)
	for itr in range (0,1):
		string_concat(num_items)

        for t_itr in times:
		times1.append(t_itr)
	times = []

	for itr in range (0,1):
		append_and_join(num_items)

	for t_itr in times:
		times2.append(t_itr)
	times = []

	for itr in range (0,1):
		list_comprehension_and_join(num_items)

	for t_itr in times:
		times3.append(t_itr)
	times = []

	for itr in range (0,1):
		generator_join(num_items)

	for t_itr in times:
		times4.append(t_itr)
	times = []
	num_items *=scale


# This could be logged using the > out.log
print (times1)
print (times2)
print (times3)
print (times4)

time_line = [0.0,num_items,num_items*scale,num_items*10.0*scale, num_items*100.0*scale, num_items*1000.0*scale, num_items*10000.0*scale]
print(time_line)

#Graph results
line1 = plt.plot(time_line, times1, label='string_concat', color='green', marker='o')
line2 = plt.plot(time_line, times2, label='append_and_join', color='red', marker='o')
line3 = plt.plot(time_line, times3, label='list_comprehension_and_join', color='blue', marker='o')
line4 = plt.plot(time_line, times4, label='generator_and_join', color='orange', marker='o')

plt.legend(loc='upper left')
plt.xlabel('time (s)')
plt.ylabel(' num of items')
plt.title('Time Comparision of the many ways to join')
plt.grid(True)
plt.savefig("test.png")
plt.show()


