import inspect
import string

def is_str(value):
	return isinstance(value,str)

for n, v in inspect.getmembers(string, is_str):
	if n.startswith('_'):
		continue
	print('%s=%r\n' %(n,v))

