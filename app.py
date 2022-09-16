import time
import urllib.request

run = True
minutes = 0

while run:
    time.sleep(60)
    minutes += 1
    if minutes == 1:
        print(f'{minutes} minute has elapsed.')
    elif (minutes > 1) and (minutes < 4):
        print(f'{minutes} minutes have elapsed')
    elif minutes == 25:
        page = urllib.request.urlopen('http://www.taylorbish.com')
        page.read()
        minutes = 0
        print("Page loaded")