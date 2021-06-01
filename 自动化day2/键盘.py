from selenium import  webdriver
from selenium.webdriver import ActionChains
import  time

driver = webdriver.Chrome()


driver.get("https://www.baidu.com")
driver.maximize_window()

a = ActionChains(driver)
ele = driver.find_element_by_xpath("//*[@id='kw']").click()
a.key_down("a").key_down("b").perform()


