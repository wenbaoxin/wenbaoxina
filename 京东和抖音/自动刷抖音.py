#encoding = utf-8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

server = r'http://localhost:4723/wd/hub'
desired_capabilities = {
    "platformName": "Android",
    "platfromVersion": "7.1.2",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}
driver = webdriver.Remote(server,desired_capabilities)
time.sleep(10)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/a-8").click()
time.sleep(5)
while True:
    # TouchAction(driver)  .press(x= 434, y= 1300) .move_to(x= 480, y= 309).release().perform()
    driver.swipe(start_x=434,start_y=1300,end_x=480,end_y=309,duration=500)
    time.sleep(7)

driver.quit()

