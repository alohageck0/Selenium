__author__ = 'royalfiish'
from selenium import webdriver

wd = webdriver.Firefox()
wd.get("http://www.beepi.com")


wd.quit()