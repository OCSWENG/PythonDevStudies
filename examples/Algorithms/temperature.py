
import argparse

def fahrenheit(temperature):
	return ((float(9)/5)*temperature + 32)

def celsius(temperature):
	return (float(5)/9)*(temperature - 32)

representC = ['c','celsius']

def isCelsius(metric):
	subject = str.lower(metric)
	for item in representC:
		if (subject == item):
			return True
	return False


representF = ['f','fahrenheit']
def isFahrenheit(temperature):
        subject = str.lower(metric)
        for item in representF:
                if (subject == item):
                        return True
        return False

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Temperature Converter:')
	# choices=['C','c','F','f']
	parser.add_argument('--metric', action="store", choices=['C','c','F','f'], required=True,dest="metric")
	parser.add_argument('--temperature', action="store", type=int, required=True, dest="temperature")

	given_args = parser.parse_args()
	temperature = given_args.temperature
	metric = given_args.metric
	convertTemperature = -1
	output = "Temperature is "
	if(isCelsius(metric)):
		convertTemperature = celsius(temperature)
		output += str(convertTemperature) + " C"
	elif(isFahrenheit(metric)):
		convertTemperature = fahrenheit(temperature)
		output += str(convertTemperature) + " F"
	else:
		print("unable to determine if it was Celsius or Fahrenheit ", given_args)
		exit()

	print(output)

