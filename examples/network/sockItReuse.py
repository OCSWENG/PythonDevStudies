import socket
import sys


def reuse_sock_addr(port):
	# Enable the SO_REUSEADDR option
	sockIt.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
	new_state = sock.getsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR )


	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind( ('', port) )
	s.listen(1)

	print("Listening on port# %s" %(port))

	while True:
		try:
			connection, addr = s.accept()
			print ('Connected by %s:%s' % (addr[0], addr[1]))
		except KeyboardInterrupt:
			break
			except socket.error, msg:
				print ('%s' % (msg))

