from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r"H:/自动化/练习的html/练习的html/弹框的验证/dialogs.html")
driver.maximize_window()
driver.find_element_by_id("confirm").click()
driver.switch_to.alert.dismiss()
time.sleep(3)
driver.quit()