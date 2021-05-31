from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r"H:/自动化/练习的html/练习的html/main.html")
driver.maximize_window()
driver.switch_to.frame("frame")
driver.find_element_by_id("input1").send_keys("wenbaoxin")
time.sleep(3)
driver.quit()