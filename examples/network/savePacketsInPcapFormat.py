
import os
from scapy.all import *

pkts = []
iter = 0
pcapnum = 0

def write_cap(x):
	global pkts
	global iter
	global pcapnum
	pkts.append(x)
	iter += 1
	if iter == 3:
		pcapnum += 1
		pname = "pcap%d.pcap" %pcapnum
		wrpcap(pname, pkts)
		pkts = []
		iter = 0

if __name__ == '__main__':
	print "Started packet capturing and dumping ... PRESS CTRL+C to exit"
	sniff(prn=write_cap)

	print "Testing the dump file....."
	dump_file = "./pcap1.pcap"

	if os.path.exists(dump_file):
		print "dimp file %s found." %dump_file
		pkts = sniff(offline=dump_file)
		count =0
		while (count <=2):
			print "----- DUMPING pkt:%s ----" %count
			print hexdump(pkts[count])
			count += 1
	else:
		print "dump file %s not found." %dump_file

