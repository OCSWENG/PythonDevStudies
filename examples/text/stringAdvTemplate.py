import string

class MyTemplate(string.Template):
	delimiter = '%'
	idpattern = '[a-z]+_[a-z]+'

templateText = """
	Delimeter : %%
	Replaced  : %with_underscore
	Ignored   : %notunderscored
"""

d= {
	'with_underscore': 'replaced',
	'noteunderscored': 'not replaced',
}

template = MyTemplate(templateText)

print("Modified ID pattern:")

print(template.safe_substitute(d))


