
import schedule_test
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
# 静默模式
# option.add_argument('headless')


def job1():
    print('Job5-startTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    time.sleep(3)
    print('Job5-endTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    driver = webdriver.Chrome(options=option)
    driver.get('https://www.baidu.com')
    # driver.find_element_by_id('http://www.baidu.com').click()

if __name__ == '__main__':
    # schedule.every().day.at('10:10').do(job1)
    print('Job5-startTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.get('https://jtoa.founder.com/wui/main.jsp')
    driver.implicitly_wait(5)
    print('Job5-endTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    driver.find_element_by_xpath('//*[@id="loginid"]').send_keys('yuan.zk@founder.com')
    driver.find_element_by_xpath('//*[@id="userpassword"]').send_keys('184')
    driver.find_element_by_xpath('//*[@id="login"]').click()
    driver.implicitly_wait(10)
    print('Job5-endTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    kq = driver.find_element_by_name("kaoqin")
    kq.find_element_by_xpath("//option[@value='2']").click()
    driver.implicitly_wait(1)
    # driver.find_element_by_xpath('//*[@id="tdSignInfo1"]/div/div').click()
    # button = driver.find_element_by_xpath('//*[@id="tdSignInfo1"]/div').find_element_by_tag_name('div')
    button = driver.find_elements_by_id('tdSignInfo1').pop(1).find_element_by_tag_name('div').find_element_by_tag_name('div')
    # button.send_keys(Keys.ENTER)
    button.click()
    driver.implicitly_wait(2)

    print("click option_2 complete")
    kq.find_element_by_xpath("//option[@value='3']").click()
    driver.implicitly_wait(1)
    button.click()
    print('Job5-endTime:{}, test {}',(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')), 'end ...')

