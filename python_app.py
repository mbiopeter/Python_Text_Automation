from credentials import mobile_number
import requests
import schedule
import time

def send_massage():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message':'May God bless you for being there for me!',
        'key': 'textbelt',
    })
    print(resp.json())


schedule.every().day.at("10:00").do(send_massage)

while True:
    schedule.run_pending()
    time.sleep(1)