# coding = utf-8
from selenium import webdriver
from list01 import testlist

from time import sleep, ctime
import os
from selenium.webdriver.common.by import By

myoptions = webdriver.ChromeOptions()
myoptions.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_driver_binary = "D:\\sorttest\chromedriver.exe"
driver = webdriver.Chrome(options=myoptions)
driver.get("https://www.baidu.com")
sleep(2)

for i in range(0, len(testlist)):
    driver.find_element(by=By.ID, value="kw").clear()
    driver.find_element(by=By.ID, value="kw").send_keys(testlist[i])
    driver.find_element(by=By.ID, value="su").click()
    sleep(3)
driver.quit()
