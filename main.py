from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

driver.get("https://w2.sfgame.net/")
# all_window_handles = driver.window_handles
# driver.switch_to.window(all_window_handles[0])

try:
    cookies = WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
    )
    cookies.click()
    element = driver.find_element_by_css_selector("#webgl-element")
    element_text = driver.execute_script("return arguments[0].innerText;", element)
    print(element_text)
finally:
    time.sleep(50)
    driver.quit()

time.sleep(50)

username = driver.find_element_by_name("username")
username.send_keys("Luis04s")
password = driver.find_element_by_name("password")
password.send_keys("jkoSEKEC322")

login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()

time.sleep(10)

element = driver.find_element_by_xpath("//button[text()='Click Here']")
element.click()
