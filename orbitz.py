__author__ = 'royalfiish'
from selenium import webdriver
import time

# Create object webdriver
wd = webdriver.Firefox()

# go to url
wd.get('http://www.orbitz.com')

# select flight radio-button
wd.find_element_by_id('search.type.air').click()
time.sleep(4)

# type LAX in origin
wd.find_element_by_name('ar.rt.leaveSlice.orig.key').send_keys('LAX')

# type BOS in destination
wd.find_element_by_name('ar.rt.leaveSlice.dest.key').send_keys('BOS')

# choose departure date
wd.find_element_by_name('ar.rt.leaveSlice.date').send_keys('07/31/15')

# choose return date
wd.find_element_by_name('ar.rt.returnSlice.date').send_keys('08/31/15')

# click search
wd.find_element_by_name('search').click()
time.sleep(8)

# store minimum price
price = wd.find_element_by_xpath("//*[@id='preMatrix']/div[4]/div[2]/span").text

print(price)
wd.quit()