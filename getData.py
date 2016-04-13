# import requests
import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
import sys

baseURL = "http://toronto.virginradio.ca/"

driver = webdriver.PhantomJS() # or add to your PATH
driver.set_window_size(1024, 768) # optional
driver.get(baseURL)
driver.save_screenshot('screen.png') # save a screenshot to disk
element = driver.find_element_by_id("mh_txtSong")
print "finished get"
print element.text
