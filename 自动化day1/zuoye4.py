from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r"H:/自动化/练习的html/练习的html/跳转页面/pop.html")
driver.maximize_window()
driver.find_element_by_id("goo").click()
# driver.switch_to.alert.accept()
time.sleep(3)
driver.quit()