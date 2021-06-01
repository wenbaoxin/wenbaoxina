from selenium import webdriver
from selenium.webdriver import  ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://www.suning.com/")
driver.maximize_window()
time.sleep(2)
# 搜索
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("秋裤")
driver.find_element_by_id("searchSubmit").click()
time.sleep(3)

driver.find_element_by_xpath("//*[@id='0070150037-178402040']/div/div/div[2]/div[2]/a").click()
time.sleep(6)
win = driver.window_handles
driver.switch_to.window(win[1])

driver.find_element_by_xpath("//*[@id='J-TZM']/dl[1]/dd/ul/li[2]/a/span").click()
driver.find_element_by_xpath("//*[@id='J-TZM']/dl[2]/dd/ul/li[1]/a").click()
driver.find_element_by_xpath("//*[@id='addCart']").click()




