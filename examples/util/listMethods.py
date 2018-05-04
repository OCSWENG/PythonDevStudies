import os
import sys
import socket
import builtins
#dir(builtins) 

def listBuiltInFunctions():
	builtInFunc = ['abs','dict','help','min','setattr','all','dir','hex','next','slice','any','divmod','id','object','sorted','ascii','enumerate','input','oct','staticmethod','bin','eval','int','open','str','bool','exec','isinstance','ord','sum','bytearray','filter','issubclass','pow','super','bytes','float','iter','print','tuple','callable','format','len','property','type','chr','frozenset','list','range','vars','classmethod','getattr','locals','repr','zip','compile','globals','map','reversed','__import__','complex','hasattr','max','round','delattr','hash','memoryview', 'set']
	for item in builtInFunc:
		yield item

def processCmd (command):
	print("processCmd")

if __name__ == '__main__':

	# list modules
	#select module
	#list methods
	cont = True
	while(cont == True):
		items = listBuiltInFunctions()
		
		for item in items:
			print(item)
			choice = input("Next(n) Pick(p) or Stop(s)")
			if(choice == "n"):
				print("Next selected ")
				continue
			elif (choice == "p"):
				print("Picking %s" %(item))
				processCmd(item)
				break	
			elif (choice == "s"):
				print("Stopping ....")
				cont = False
				break	
			else:
				cont = False
				break	


