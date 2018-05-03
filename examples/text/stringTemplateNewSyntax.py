import string

class MyTemplate(string.Template):
	delimiter = '{{'
	pattern = r'''
	\{\{(?:
	(?P<escaped>\{\{)|
	(?P<named>[_a-z][_a-z0-9]*)\}\}|
	(?P<braced>[_a-z][_a-z0-9]*)\}\}|
	(?P<invalid>)
	)
	'''

templateText = """
	{{{{
	{{var}}
"""

template = MyTemplate(templateText)

print("Modified ID pattern:")

print('MATCHES:', template.pattern.findall(template.template))
print('SUBSTITUTED:', template.safe_substitute(var='replacement'))


