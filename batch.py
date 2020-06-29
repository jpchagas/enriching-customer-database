import requests
import schedule
import time
 
def batch():
    requests.get('https://ecdserver.herokuapp.com/update')
    print("Requested")

schedule.every(1).minutes.do(batch)

while 1:
    schedule.run_pending()
    time.sleep(1)
