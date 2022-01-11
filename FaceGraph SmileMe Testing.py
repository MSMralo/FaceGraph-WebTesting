#!/usr/bin/env python
# coding: utf-8

# # Smile TEST FG202121

# In[1]:


#packages
import random
import time
import urllib
import bs4
import requests
import os
import pandas as pd
import numpy as np
import matplotlib as lib
import re
from collections import OrderedDict

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from urllib.parse import urljoin


# In[2]:


options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--remote-debugging-port=9222')

wb = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)
wb.get("https://facegraphidqa.azurewebsites.net/Account/Login")
#wb.close()


# In[3]:


def login():
    config = {
        'EMAIL': '011416',
        'PASSWORD': '123456'
    }
    
    elem = wb.find_element(By.ID,"Username")
    elem.clear()
    elem.send_keys(config['EMAIL'])
    elem = wb.find_element(By.ID,'Password')
    elem.clear()
    elem.send_keys(config['PASSWORD'])
    elem = wb.find_element(By.ID,'AutoVerificationCode')
    elem.click()
    elem = wb.find_element(By.ID,'btnSubmit')
    elem.click()
    time.sleep(8)
    try:
        elem = wb.find_element(By.CSS_SELECTOR,'div.welcome_page > div.user_account > span:nth-child(2)')
        elem.click()
        print("welcome page")
    except:
        print("No welcome page")
    time.sleep(10)
    try:
        elem = wb.find_element(By.CLASS_NAME,'chankya-ham-icon')
        elem.click()
        print("menu clicked")
        print("login success")
    except:
        print("login faild")
        print("error clicking menu")
    time.sleep(2)
    try: #scroll down with keys
        elem = wb.find_element(By.TAG_NAME,'html')
        elem.send_keys(Keys.PAGE_DOWN)
        print("scrolled down")
    except:
        print("faild to scroll down")
    time.sleep(2)
    try:
        elem = wb.find_element(By.PARTIAL_LINK_TEXT,'Manage Attendance')
        elem.click()
        print("Manage tab clicked")
    except:
        print("faild to click on Manage tab")
    time.sleep(2)
    try:
        elem = wb.find_element(By.PARTIAL_LINK_TEXT,'Students')
        elem.click()
        print("Students tab loaded")
    except:
        print("faild to click on Students tab")
    time.sleep(5)
    try:
        elem = wb.find_element(By.CLASS_NAME,'close-mobile-menu')
        elem.click()
        print("menu closed")
    except:
        print("faild to close menu")


# In[4]:


def addSignIn(h,m):
    minutes=m
    hour=h-8
    n,t=1,1
    elem = wb.find_element(By.CLASS_NAME,'btn-success')
    elem.click()
    time.sleep(2)
    elem = wb.find_element(By.ID,'childId')
    elem.click()
    time.sleep(2)
    elem.send_keys(Keys.DOWN)
    elem.click()
    time.sleep(2)
    elem = wb.find_element(By.ID,'signedInAt')
    elem.click()
    time.sleep(2)
    elem = wb.find_element(By.CLASS_NAME,'fa-angle-up')
    while n<=hour:
        elem.click()
        n+=1
    time.sleep(2)
    elem = wb.find_element(By.CSS_SELECTOR,'div.ui-minute-picker > a:nth-child(1) > span')
    while t<=minutes:
        elem.click()
        t+=1
    time.sleep(3)
    elem = wb.find_element(By.CLASS_NAME,'ui-clickable')
    elem.click()
    time.sleep(2)
    elem = wb.find_element(By.ID,'signedInBy')
    elem.click()
    time.sleep(2)
    elem.send_keys(Keys.DOWN)
    elem.click()
    time.sleep(2)
    try: #scroll down with keys
        elem = wb.find_element(By.TAG_NAME,'html')
        elem.send_keys(Keys.PAGE_DOWN)
        print("scrolled down")
    except:
        print("faild to scroll down")
    try: #SAVE
        elem = wb.find_element(By.CSS_SELECTOR,'div.col-md-12.col-lg-6.col-xl-4.mb-3 > button')
        elem.click()
        time.sleep(2)
        print("Temperature is Optional verified")
        print("Signed in Saved for Student1 at "+str(h)+":"+str(m))
        return True
    except:
        print("Signed in Not Saved for Student1")
        return False


# In[5]:


login()


# In[7]:


if addSignIn(10,18) is True:
    if addSignIn(10,19):
        print("Issue: Two Signed in for same student accepted")
else:
        print("NO Issue")


# In[8]:


wb.close()


# ## Conclusion of this Test
# ## *Issues
# ### -We have two sign in for the same student which indicate a problem with the backend
# ## *Working points
# ### -login is working correctly
# ### -Temperature is Optional
# ### -We can't add two sign in with the same time 

# In[ ]:




