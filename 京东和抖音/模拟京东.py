#encoding = utf-8
from appium import webdriver
import time

server = r'http://localhost:4723/wd/hub'
desired_capabilities = {
    "platformName": "Android",
    "platfromVersion": "7.1.2",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.jingdong.app.mall",
    "appActivity": "com.jingdong.app.mall.main.MainActivity"
}
driver = webdriver.Remote(server,desired_capabilities)
driver.find_element_by_id("com.jingdong.app.mall:id/bqd").click()
time.sleep(3)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[3]/android.widget.ViewFlipper").click()
time.sleep(3)
driver.find_element_by_id("com.jd.lib.search.feature:id/zw").send_keys("裙子").click()
time.sleep(3)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView").click()
time.sleep(3)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout").click()
time.sleep(3)
driver.find_element_by_id("com.jd.lib.productdetail.feature:id/pd_invite_friend").click()
time.sleep(3)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.TextView").click()
time.sleep(3)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout/android.view.ViewGroup").click()
