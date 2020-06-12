import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_driver = "F:/install/env/third-driver/chromedriver_win32/chromedriver.exe"
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
# print('current window url: s%', driver.current_url)

handles = driver.window_handles
for handle in handles:  # 历遍所有标签的句柄
    driver.switch_to.window(handle)  # 通过句柄切换到该浏览器的标签
    if 'Citrix XenApp' in driver.title:    #driver.title当前标签名
        print(driver.title)
        break #退出循环
print(driver.title, driver.current_window_handle)


# driver.implicitly_wait(5)
button_back = driver.find_element_by_id("loginPageLink")
button_back.click()
#driver.implicitly_wait(5)
time.sleep(2)

input_user = driver.find_element_by_id("user")
input_pwd = driver.find_element_by_id("password")

# TODO by key
input_user.send_keys("99005172")
input_pwd.send_keys("yzk123ASDL")

time.sleep(1)
driver.implicitly_wait(1)
driver.find_element_by_id("btnLogin").click()

print("login complete")
time.sleep(3)

driver.refresh()  #刷新页面

driver.find_element_by_xpath('//*[@id="idCitrix.MPS.Desktop.XD76.DG_005fWIN7X64_005fNAS02_0020_0024S30-28"]').click()

print("opend window ...")
driver.quit()
