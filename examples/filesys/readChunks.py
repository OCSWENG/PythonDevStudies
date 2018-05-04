
import os

def readBytes (file, size=512):
	while True:
		data = f.read(size)
		if not data:
			break
		yield data

# size = 512
# with open(fileName) as file:
	for data in readBytes(file)
		processData(data)
