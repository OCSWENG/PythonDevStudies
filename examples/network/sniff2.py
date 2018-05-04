import socket
import struct
import binascii

# socket.htons shows the protocol of interest, 0x0800 is ETH_P_IP
# find it in /usr/include/linux if_ether.h
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

while True:
	# create a buffer of 2K in a tuple
	pkt = s.recvfrom(2048)
	# take the first 14 bytes = Ethernet frame
	ethhead = pkt[0][0:14]
	
	# ! = show network bytes
	# 6s = show 6 bytes
	# 2s = show 2 bytes
	eth = struct.unpack("!6s6s2s", ethhead)
	print "********Ethernet Frame **********"
	print "dest MAC:{}".format(binascii.hexlify(eth[0]))
	print "src MAC: {}".format(binascii.hexlify(eth[1]))
	binascii.hexlify(eth[2])

	# take the bytes 14 to 34 or 20 bytes
	ipheader = pkt[0][14:34]

"""
	Interested in TTL
	ip_hdr = struct.unpack("!8sB3s4s4s", ipheader)
	print "-------- IP ---------"
	print "TTL :{}".format(ip_hdr[1])
	print "Source IP: {}".format(socket.inet_ntoa(ip_hdr[3]))
	print "Dest IP: {}".format(socket.inet_ntoa(ip_hdr[4]))
"""
	# upack in 3 parts {dest(12s), source(4s), address(4s)}
	ip_hdr = struct.unpack("!12s4s4s", ipheader)
	print "********* IP ************"
	print "Source IP: {}".format(socket.inet_ntoa(ip_hdr[1]))
	print "Dest IP: {}".format(socket.inet_ntoa(ip_hdr[2]))

	print "******** TCP ***********"
	tcpheader = pkt[0][34:54]

	# !HH16s 3 parts {Source, Dest, port number}
	# !HH9ss6s 4 parts {Source, Dest, port number, flag}
	tcp_hdr = struct.unpack("!HH9ss6s", tcpheader)
	print "Source Port {}".format(tcp_hdr[0])

	print "Dest Port {}".format(tcp_hdr[1])
	print "FLAG: {}".format(binascii.hexlify{tcp_hdr[3])

	print pkt[0][54:]

