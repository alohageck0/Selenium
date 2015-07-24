__author__ = 'royalfiish'
from selenium import webdriver
import time

wd = webdriver.Firefox()
wd.get("http://www.beepi.com")
time.sleep(5)

# click BUY
wd.find_element_by_xpath(".//*[@id='headerlinks']/li[12]/a").click()


wd.find_element_by_id('searchInput').send_keys("volkswagen")
time.sleep(2)
wd.quit()
