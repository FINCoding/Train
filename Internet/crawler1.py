#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:\Program Files\chromedriver\chromedriver.exe')
browser.get('http://quotes.toscrape.com/')

elements = browser.find_elements_by_class_name('text')
for element in elements:
    text = element.text
    print(text)cd cd