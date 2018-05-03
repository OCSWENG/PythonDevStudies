#pip install ntplib
import ntplib
from time import ctime

def get_time():
	ntp_client = ntplib.NTPClient()
	response = ntp_client.request('pool.ntp.org')
	time1 =  ctime(response.tx_time)
	print(time1)

if __name__ == '__main__':
	get_time()

