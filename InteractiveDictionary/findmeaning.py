import json
from difflib import get_close_matches
import argparse

data = {}

# get the word
word = ''

def clean_word(word):
	newWord =""
	definition = "" 
	toQuit=""
	possibleMatches = get_close_matches(word, data.keys())
	while True:
		select = 0
		for item in possibleMatches:
			print ( "select #%d for : %s" %(select, item))
			select += 1
		if(len(possibleMatches) < 1):
			print("There was no possible matches, Try again:")
			return (toQuit,definition)
		# wait for user response
		choice = input("A negative value to quit or a Choice? ")
		if (choice.isdigit() == False):
			print( "Problem: the choice exceeded the available choices. Select again")	
		else:
			intChoice = int(choice)
			if (choice == ""):
				 print( "Problem: the choice exceeded the available choices. Select again")
			elif(intChoice > len(data.keys())):
				print( "Problem: the choice exceeded the available choices. Select again")
			elif(intChoice < 0):
				return (toQuit,definition)
			else:
				newWord = possibleMatches[intChoice]
				definition = data[newWord]
				break
	return (newWord, definition)


def findDefinition(word):
	cleanWord, definition  = clean_word(word)
	if( cleanWord != ""):
		print("Found the definition of :",cleanWord)
		print(definition[0])

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Temperature Converter:')
	parser.add_argument('--lookup', action="store", default="", required=False,dest="lookUpWord")
	parser.add_argument('--interactive', action="store", choices=[0,1], default=1, type=int, required=False, dest="interact")

	given_args = parser.parse_args()
	interact = given_args.interact
	with open ("data.json", 'r') as fh:
		data = json.load(fh)

		if (interact == 1):
			print(" *****   Interactive Dictionary *****")
			print('         ----------------------      ')
			print(' *****   Enter stopApp to quit')

			while True:
				word = input("Enter a word or command: stopApp %")
				if (word == 'stopApp'):
					print('Stopping ....')
					break
				if(word.isalpha() == True):
					findDefinition(word)
		else:
			word = given_args.lookUpWord
			findDefinition(word)

