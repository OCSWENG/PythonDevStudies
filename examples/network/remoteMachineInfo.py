import socket

def remoteMachineInfo (remote_host):
	try:
		ipaddr = socket.gethostbyname(remote_host)
		return {"remote_host:" : remote_host, "ipAddr": ipaddr}
	except (socket.error, Exception) as e:
		return {"remote_host": remote_host, "ipAddr": ipaddr, "errors": e}

if __name__ == '__main__':
	value  = remoteMachineInfo('www.python.org')
	print(value)

