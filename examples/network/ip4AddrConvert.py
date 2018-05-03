import socket
from binascii import hexlify


def convert_ip4_address(ipAddrArray):
	for ipAddr in ipAddrArray:
		packed_ipAddr = socket.inet_aton(ipAddr)
		unpacked_ipAddr = socket.inet_ntoa(packed_ipAddr)
		print ("IP Address: %s => Packed: %s, Unpacked: %s"\
			%(ipAddr, hexlify(packed_ipAddr), unpacked_ipAddr))


if __name__ == '__main__':
	ipAddrArray = ['127.0.0.1', '192.168.0.1']
	convert_ip4_address(ipAddrArray)



