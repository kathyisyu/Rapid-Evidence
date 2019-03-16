from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import re
import pandas as pd
import os

import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup 

import scholarly #uses the google scholar interface 

keywords = " Transcatheter or surgical aortic-valve replacement"
search = scholarly.search_pubs_query(keywords) #searches keywords within google scholars 

numbercited = 0 #records the number of citations 
url = ""#variable that stores the url 

while search:
   try:
       obj = next(search)
       cite = obj.citedby
       ur = obj.bib['url']

       if cite > numbercited:
            url = ur 
            numbercited = cite 
   except:
       break

print(url)
#Launch url through selenium via the Chrome Web Browser 
# create a new Chrome session 
driver = webdriver.Chrome("C:\\Users\\ymtlj\\Desktop\\chromedriver.exe").get(url).implicitly_wait(30)
