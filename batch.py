import requests
import schedule
import time


def batch():
    requests.get('http://localhost:5000/update')

schedule.every(1).minutes.do(batch)

while 1:
    schedule.run_pending()
    time.sleep(1)