import time
from datetime import datetime as dt

hostsTemp = r"C:\Users\Cyrus\Desktop\PyProj\websiteBlocker\hosts"
hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websiteList=[
    "www.facebook.com",
    "www.youtube.com",
    "www.whatsapp.com",
    "www.twitter.com",
    "www.gmail.com",
    "outlook.live.com",
    "www.wish.com"
]
while True:
    #From 8AM to 5PM
    if dt(dt.now().year,dt.now().month,dt.now().day, 5) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day, 17):
        print("Working Hours!...")
        with open(hostsPath, 'r+') as file:
            content = file.read()
            for website in websiteList:
                if website in content:
                    pass
                else:
                    file.write(redirect + "       " + website +"\n")
    else:
        with open(hostsPath, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websiteList):
                    file.write(line)
                file.truncate()
        print('Time to have fun!')
    time.sleep(5)