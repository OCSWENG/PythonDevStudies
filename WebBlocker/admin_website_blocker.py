import time
from datetime import datetime as dt

hosts_temp=r"./hosts"
# replace hosts_temp with hostPath then start the process in administration level 
# sudo crontab -e 
# @reboot python3 /home/dir1/dir2/dir3/admin_website_blocker.py

hostPath="/etc/hosts"
redirect="127.0.0.1"

websiteList=["www.facebook.com","www.youtube.com","http://www.bbc.com","www.mail.goole.com/mail"]

#list generation
finalList = [redirect + ' ' + i for i in websiteList]

beginWorkHour = 8
endWorkHour = 16

while True:
    beginWorkTime = dt(dt.now().year,dt.now().month,dt.now().day, beginWorkHour)
    endWorkTime = dt(dt.now().year,dt.now().month,dt.now().day, endWorkHour)
    
    # once work commences write to the host file to block websites.
    if ( beginWorkTime < dt.now() < endWorkTime ):
        # print("Work TimeFrame ...")
        
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in websiteList:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else: # remove items in a file using the truncate 
        with open(hosts_temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websiteList):
                    file.write(line)
            file.truncate()
        # print("Non Work TimeFrame ...")
    time.sleep(5)
