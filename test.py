#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:16:33 2019

@author: axtel
"""

#Open Google in Safari

#import selenium
from selenium import webdriver

driver = webdriver.Safari()
driver.get("http://www.google.com")

from Ipython.display import Image
Image('chrome.jpg')
