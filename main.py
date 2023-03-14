from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()


driver.get("https://w2.sfgame.net/")
time.sleep(10000)

username = driver.find_element_by_name("username")
username.send_keys("Sir Ritteboli")
password = driver.find_element_by_name("password")
password.send_keys("jkoSEKEC322")

login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

time.sleep(10)

element = driver.find_element_by_xpath("//button[text()='Click Here']")
element.click()
