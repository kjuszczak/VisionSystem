from selenium import webdriver
import time
DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
driver.get("https://www.google.pl/maps/place/32-082+Kobylany/@50.1493135,19.7532561,2306m/data=!3m1!1e3!4m5!3m4!1s0x4716f78b5aa90fa1:0x270433a9e92382fc!8m2!3d50.1493144!4d19.7620109")
time.sleep(2)
driver.find_element_by_xpath("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc']").click()
time.sleep(10)
driver.find_element_by_xpath("//a[@class='gsst_a']").click()
time.sleep(2)
driver.find_element_by_xpath("//button[@aria-label='Zamknij']").click()
screenshot = driver.save_screenshot('my_screenshot.png')
driver.quit()