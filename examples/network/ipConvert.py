import socket


def convertInt(data):
	try:
		print("DATA: %s" %(data))
		print("BYTE ORDER %s" %(socket.ntohl(data)))
		print("Network BYTE ORDER %s" %(socket.htonl(data)))
	except Exception as e:
                print("EXCEPTION: %s" %(e))

def convertDblByte(data):
	try:
        	print("DATA: %s" %(data))
        	print("BYTE ORDER %s" %(socket.ntohs(data)))
        	print("Network BYTE ORDER %s" %(socket.htons(data)))
	except Exception as e:
		print("EXCEPTION: %s" %(e))


if __name__ == '__main__':
	data = 2987

	convertInt(data)
	convertDblByte(data)

	
