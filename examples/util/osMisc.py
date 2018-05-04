import os

print(' os.path {}'.format(os.path)) # is either posixpath or ntpath
print(' os.name {}'.format(os.name)) # is either 'posix', 'nt' or 'ce'.
print(' os.curdir {}'.format(os.curdir)) # string representing the current directory ('.' or ':')
print(' os.pardir {}'.format(os.pardir)) # representing the parent directory ('..' or '::')
print(' os.sep {}'.format(os.sep))  # pathname separator ('/' or ':' or '\\')
print(' os.extsep {}'.format(os.extsep)) # is the extension separator (always '.')
print(' os.altsep {}'.format(os.altsep)) # is the alternate pathname separator (None or '/')
print(' os.pathsep {}'.format(os.pathsep)) # is the component separator used in $PATH etc
print(' os.linesep {}'.format(os.linesep)) #line separator in text files ('\r' or '\n' or '\r\n')
print(' os.defpath {}'.format(os.defpath)) # the default search path for executables
print(' os.devnull {}'.format(os.devnull)) # the file path of the null device ('/dev/null', etc.)

PATHS = [
	'/one/two/three',
	'/one/two/three',
	'/',
	'.',
	'',
]

for path in PATHS:
	print('{!r:>17} : {}'.format(path, os.path.split(path)))

print('commonPrefix {}'.format(os.path.commonprefix(PATHS)))


PATHS = [
	'/one/two/xyz',
	'/one/two/zyx',
	'/one/two/abc',
	'/one/two/cba',
]

print ('commonPrefix {}'.format(os.path.commonprefix(PATHS)))

PATHS = [
	'filename.txt',
	'filename',
	'/path/to/filename.txt',
	'/',
	'',
	'my-archive.tar.gz',
	'no-extenstion',
]

for path in PATHS:
	print('{!r:>21} : {!r}'.format(path,os.path.splitext(path)))


PATHS = [
	('one','two','three'),
	('/','one','two','three'),
	('/one','/two','/three'),
]

for parts in PATHS:
	print(' {} : {!r}'.format(parts, os.path.join(*parts)))

