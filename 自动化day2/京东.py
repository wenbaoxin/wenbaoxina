from selenium import webdriver
from selenium.webdriver import  ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://www.jd.com/")
driver.maximize_window()
time.sleep(2)

driver.find_element_by_link_text("你好，请登录").click()
time.sleep(8)

driver.find_element_by_xpath("//*[@id='key']").send_keys("裙子")
driver.find_element_by_xpath("//*[@id='search']/div/div[2]/button/i").click()
time.sleep(8)
driver.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[3]/div/div[4]/a/em").click()
time.sleep(3)

win = driver.window_handles
print(win)
driver.switch_to.window(win[1])


driver.find_element_by_xpath("//*[@id='choose-attr-1']/div[2]/div[4]/a/img").click()
driver.find_element_by_xpath("//*[@id='choose-attr-2']/div[2]/div[2]/a").click()
driver.find_element_by_xpath("//*[@id='choose-baitiao']/div[2]/div[1]/div[1]/a").click()
driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()