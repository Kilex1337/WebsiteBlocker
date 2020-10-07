import time
from datetime import datetime as dt

hosts_temp = r"D:\Aleksa\python vezbe 2\Website Blocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.instagram.com", "instagram.com", "www.facebook.com", "facebook.com",
                "www.twitter.com", "twitter.com", "www.twitch.tv", "twitch.tv"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Working hours...")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("You finished with your work today, it's your free time")
    time.sleep(300)

