import string

values = {'var' : 'foo'}
template = string.Template("""
Variable	: $var
Escape		: $$
variable in text: ${var}iable
""")

print ('TEMPLATE', template.substitute(values))

sVal = """
Variable	: %(var)s
Escape		: %%
Variable in text: %(var)siable
"""

print('INTERPOLATION', sVal % values)

sVal = """
Variable	: {var}
Escape		: {{}}
Variable in text: {var}iable
"""

sVal = """
Variable	: {var}
Escape		: {{}}
Variable in text: {var}iable
"""

print('FORMAT:', sVal.format(**values))

