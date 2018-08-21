#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:\Program Files\chromedriver\chromedriver.exe')
browser.get('https://pegast.ru/')
elementWhere = browser.find_element_by_class_name('search-form-field__input')
elementWhere.send_keys('Турция')
print("привет")
# elementFrom = browser.find_element_by_name('closeonclickoutsideoresc')
elementFrom = browser.find_element_by_class_name("pgs-dropdown_opened")
all_options = elementFrom.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()
# element = browser.find_element_by_class_name("search-form-field__date")
# all_options = element.find_elements_by_tag_name("option")
# for option in all_options:
#     print("Value is: %s" % option.get_attribute("value"))
#     option.click()