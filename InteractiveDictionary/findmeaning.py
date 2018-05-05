import json
from difflib import get_close_matches

data = {}

# get the word
word = 'alpha'

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


# Interaction Section:

if __name__ == "__main__":
	print(" *****   Interactive Dictionary *****")
	print('         ----------------------      ')
	print(' *****   Enter stopApp to quit')

	with open ("data.json", 'r') as fh:
		data = json.load(fh)

		while True:
			
			word = input("Enter a word or command: stopApp %")
			if (word == 'stopApp'):
				print('Stopping ....')
				break
			if(word.isalpha() == True):
				cleanWord, definition  = clean_word(word)
				if( cleanWord != ""):
					print("Found the definition of :",cleanWord)
					print(definition[0])

