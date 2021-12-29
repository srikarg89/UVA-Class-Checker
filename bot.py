from selenium import webdriver
from selenium.common.exceptions import TimeoutException
# Waiting for it to scroll into view
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from twilio.rest import Client
import time, datetime
from secrets import ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER, MY_NUMBER

SEMESTER_URL = "https://louslist.org/page.php?Semester=1218&Type=Group&Group=APMA"
ELEMENT_PATH = '/html/body/table[2]/tbody/tr[88]/td[5]/a'

LOOP_DELAY = 900 # Check every 300 second(s)
prev_text = None

print("Starting loop")

while True:
    print("Running loop, current time is:", datetime.datetime.now())
    try:
        driver = webdriver.PhantomJS()
        driver.get(SEMESTER_URL)
        # Driver to wait until something scrolls into view
        wait = WebDriverWait(driver, 5)
        element = driver.find_element_by_xpath(ELEMENT_PATH)
        text = element.get_attribute("innerText")
        text = text.strip()
        print(text)
        if text != prev_text:
            # Save data to file
            # print("\n\n\n\n\nOMG IT CHANGED!!!", text, "\n\n\n\n\n")
            file = open("updates.txt", "a+")
            file.write(str(datetime.datetime.now()) + "\t" + text + "\n")
            file.close()

            # Send text
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            message = client.messages.create(body=text, from_=TWILIO_NUMBER, to=MY_NUMBER)
            # print(message.sid)
            prev_text = text
        
        driver.close()

    except Exception as e:
        print("Got exception:", str(e))
        file = open("errors.txt", "a+")
        file.write(str(e) + "\n\n\n")
        file.close()

    time.sleep(LOOP_DELAY)
