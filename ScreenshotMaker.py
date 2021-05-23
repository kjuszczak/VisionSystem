from selenium import webdriver
import time
import cv2

DRIVER = 'chromedriver'

def makeScreen(place):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(DRIVER, options=chrome_options)

    driver.get("https://www.google.pl/maps/")
    time.sleep(2)
    driver.find_element_by_xpath("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc']").click()
    time.sleep(5)
    driver.find_element_by_xpath("//input[@aria-label='Wyszukaj w Mapach Google']").send_keys(place)
    driver.find_element_by_xpath("//button[@aria-label='Szukaj']").click()
    time.sleep(2)

    driver.find_element_by_xpath("//button[@aria-label='Menu']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//button[@class='widget-settings-button KY3DLe-settings-zNoUyd-LgbsSe KY3DLe-settings-GU9rYd-Xhs9z']").click()

    textLength = driver.find_element_by_xpath("//label[@id='widget-scale-label']").text
    splittedText = textLength.split()
    meters = 1
    if splittedText[1] == 'km':
        meters = 1000
    value = int(splittedText[0])*meters
    zoomInFlag = True
    if value < 500:
        zoomInFlag = False

    while driver.find_element_by_xpath("//label[@id='widget-scale-label']").text != '200 m':
        if zoomInFlag:
            driver.find_element_by_xpath("//button[@id='widget-zoom-in']").click()
        else:
            driver.find_element_by_xpath("//button[@id='widget-zoom-out']").click()
        time.sleep(1)

    driver.find_element_by_xpath("//a[@class='gsst_a']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//button[@aria-label='Zamknij']").click()
    driver.find_element_by_xpath("//button[@aria-label='Menu']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//button[@class='widget-settings-button']").click()
    time.sleep(1)

    screenshot = driver.save_screenshot('my_screenshot.png')
    driver.quit()

    img = cv2.imread("my_screenshot.png")
    height, width, channels = img.shape
    y=125
    d = 125
    x=0
    w = 75
    crop_img = img[y:height-d, x:width-w]
    cv2.imwrite('processing_image.jpg', crop_img)