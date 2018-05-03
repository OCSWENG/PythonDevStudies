import string

values = {'var' : 'foo'}

template = string.Template("$var is her but $missing is not provided")

try:
	print('substitute()	:', template.substitute(values))

except KeyError as err:
	print('ERROR:', str(err))

print('safe_subsitute():', template.safe_substitute(values))

