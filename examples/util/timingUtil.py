import timeit
setup = '''
import array
a = range(1000)
b = array.array('H',a)
c = 0
'''

timer = timeit.Timer(stmt='c=b+b', setup=setup)

print("timeIt {} * {}".format(7,1000))
t1 = timer.repeat(7,1000)
print("Times {}".format(t1))

print("timeIt {} * {}".format(2,3500))
t2 = timer.repeat(2,3500)
print("Times {}".format(t2))

print("timeIt {} * {}".format(35,200))
t3 = timer.repeat(35,200)
print("Times {}".format(t3))

