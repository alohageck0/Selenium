__author__ = 'royalfiish'
from selenium import webdriver
import time

# Create object webdriver
wd = webdriver.Firefox()
wd.get('http://www.orbitz.com')
wd.find_element_by_id('search.type.air').click()
time.sleep(4)
wd.find_element_by_name('ar.rt.leaveSlice.orig.key').send_keys('LAX')
wd.find_element_by_name('ar.rt.leaveSlice.dest.key').send_keys('BOS')
wd.find_element_by_name('ar.rt.leaveSlice.date').send_keys('07/31/15')
wd.find_element_by_name('ar.rt.returnSlice.date').send_keys('08/31/15')
wd.find_element_by_name('search').click()
time.sleep(8)
price = wd.find_element_by_xpath("//*[@id='preMatrix']/div[4]/div[2]/span").text
print(price)
wd.quit()