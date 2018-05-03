import socket

def socket_blk (blockMode, ipAddr):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setblocking(blockMode)
	s.settimeout(0.5)
	s.bind((ipAddr, 0))
	socket_address = s.getsockname()
	print ("Server launched on socket: %s" %str(socket_address))

	while(1):
		s.listen(1)

if __name__ == '__main__':
	ipAddr = "127.0.0.1"
	blockMode = 0 # 1 to block 0 to unblock
	socket_blk(blockMode, ipAddr)

