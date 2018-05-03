
import socket

def machineInfo ():
	host_name = socket.gethostname()
	ip_address = socket.gethostbyname(host_name)
	return {"hostName": host_name, "IP address": ip_address}


if __name__ == '__main__':
	print (machineInfo()) 
