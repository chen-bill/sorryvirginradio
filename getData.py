# import requests
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
from twilio.rest import TwilioRestClient

baseURL = "http://toronto.virginradio.ca/"


def logData (logText):
    print logText
    with open("dataLog.txt", "a") as dataLog:
        dataLog.write(logText)
    dataLog.close()

def sendMessage(phoneNumber, bodyText):
    message = client.messages.create(to=phoneNumber, from_="+12898035279", body=bodyText)

def getSong():
    driver = webdriver.PhantomJS() # or add to your PATH
    driver.set_window_size(1024, 768) # optional
    driver.get(baseURL)
    driver.save_screenshot('screen.png') # save a screenshot to disk
    element = driver.find_element_by_id("mh_txtSong")
    return element.text


def main():
    bodyText = ""
    print "main starting"
    with open("authentication.txt", "r") as f:
        array = []
        for line in f:
            array.append(line.rstrip())

    account_sid = array[0]
    auth_token = array[1]

    client = TwilioRestClient(account_sid, auth_token)
    currentlyPlaying = getSong()
    if 'sorry' in currentlyPlaying:
        bodyText = "Money time: " + element.text.lower() + " is playing!\n"
        # sendMessage("6475232602", bodyText)
        # sendMessage("2263784509", bodyText)
        logData(bodyText)

    else:
        bodyText = currentlyPlaying + " | " + str(datetime.now()) + " | " + " sorry not sorry\n"
        logData(bodyText)

    f.close()

main();
