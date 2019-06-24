import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
print('current window url: {}', driver.current_url)
# driver.maximize_window()

# handles = driver.window_handles
# driver.switch_to.window(handles[1])

target_window = "https://jtoa.founder.com"
driver.get('https://jtoa.founder.com/wui/main.jsp')
driver.implicitly_wait(5)
kq = driver.find_element_by_name("kaoqin")
kq.find_element_by_xpath("//option[@value='3']").click()
driver.implicitly_wait(1)
button = driver.find_elements_by_id('tdSignInfo1').pop(1).find_element_by_tag_name('div').find_element_by_tag_name('div')
button.click()
driver.implicitly_wait(2)

print("click option_2 complete")
print('current window url: {}', driver.current_url)


