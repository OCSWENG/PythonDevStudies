import sys
import argparse
import socket

host = 'localhost'

def echo_client(port):

	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Connect the socket to the server
	server_address = (host, port)
	print ("Connecting to %s port %s" %(server_address))
	sock.connect(server_address)

	try:
		# Send data
		message = "Test message. This will be echoed"
		print ("Sending %s" %( message))
		sock.sendall(message)

		# Look for the response
		amt_received = 0
		amt_expected = len(message)

		while amt_received < amt_expected:
			data = sock.recv(16)
			amt_received += len(data)
			print ("Received: %s" % (data))

	except socket.errno, e:
		print ("Socket error: %s" %(str(e)))
	except Exception, e:
		print ("Other exception: %s" %(str(e)))
	finally:
		print ("Closing connection to the server")
		sock.close()

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Socket Server Example:")

	parser.add_argument('--port', action="store", dest="port",type=int, required=True)

	given_args = parser.parse_args()
	port = given_args.port
	echo_client(port)
