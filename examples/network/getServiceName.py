import socket

def find_service_name(ports, protocol):
	print("PORTS %s , protocol %s " %(ports, protocol))


	for port in ports:
		try:
			serviceName = socket.getservbyport(port, protocol)
			print("Port# %s : ServiceName: %s " %(port, serviceName))
		except Exception as e:
			print("Exception %s" %(e))


if __name__ == '__main__':
	ports = [80,100,20]
	protocol = 'tcp'

	find_service_name(ports, protocol)

	ports2 = [25,44,50]
	protocol = 'udp'
	
	find_service_name(ports2, protocol)




