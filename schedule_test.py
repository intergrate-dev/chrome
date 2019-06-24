import json
import random
import urllib.request as urlrequest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import schedule
import time
import datetime

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
print('current window url: {}', driver.current_url)


def job_1():
    print('job_1-startTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    if not purse():
        return
    print('job_1-afterpurse-time:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    punch_by_clock('1')


def job_2():
    print('job_2-startTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    if not purse():
        return
    print('job_2-afterpurse-time:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    punch_by_clock('2')


def job_3():
    print('job_3-startTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    if not purse():
        return
    print('job_3-afterpurse-time:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    punch_by_clock('3')


def job_4():
    print('job_4-startTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    if not purse():
        return
    print('job_4-afterpurse-time:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    punch_by_clock('4')


def punch_by_clock(opt_value):
    driver.get('https://jtoa.founder.com/wui/main.jsp')
    driver.implicitly_wait(5)
    kq = driver.find_element_by_name("kaoqin")
    opt = kq.find_element_by_xpath("//option[@value='" + opt_value + "']")
    opt.click()
    driver.implicitly_wait(1)
    button = driver.find_elements_by_id('tdSignInfo1').pop(1).find_element_by_tag_name('div').find_element_by_tag_name(
        'div')
    button.click()
    driver.implicitly_wait(2)
    print("click option: ", opt.text)
    print('{}, func job_1 execute complete ...', (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


def purse():
    # t_now = now + datetime.timedelta(minutes=m_r) + datetime.timedelta(seconds=s_r)
    s_r = random.choice(range(0, 43))
    time.sleep(s_r)
    print('---------------- purse time: ', s_r)
    return is_workday()


def job_by_senc():
    print('job_1-job_by_senc-startTime:%s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    if not purse():
        return
    print('--------------------- Job-by-sencond:  ---------------------',
          (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


def is_workday():
    # now = datetime.datetime.now()
    # print("weekday: {}, day: {}", now.weekday(), now.day)
    # workday_candi = range(0, 4)
    now_date = time.strftime('%Y%m%d', time.localtime())
    server_url = 'http://api.goseek.cn/Tools/holiday?date='
    url_request = urlrequest.Request(server_url + now_date)
    response = urlrequest.urlopen(url_request)
    res_json = json.loads(response.read())
    print('res_json: ', res_json)
    holi_candi = [0, 2]
    if res_json['data'] in holi_candi:
        print('today is a workday: ', res_json['data'])
        return True
    return False


if __name__ == '__main__':
    # for i in range(0, 10):
    #     r = random.choice(range(-12, 12, 2))
    #     print("r: ", r)

    # m_r = random.choice(range(-12, 12, 2))
    # s_r = random.choice(range(-30, 30, 3))
    # now = datetime.datetime.now()
    # print('now: ', now)
    # t_now = now + datetime.timedelta(minutes=m_r) + datetime.timedelta(seconds=s_r)
    # print('t_now: ', t_now)


    schedule.every().day.at('08:45:23').do(job_1)
    schedule.every().day.at('12:13:43').do(job_2)
    schedule.every().day.at('12:23:45').do(job_3)
    schedule.every().day.at('18:30:40').do(job_4)

    # schedule.every(10).seconds.do(job_by_senc)

    while True:
        schedule.run_pending()
        time.sleep(5)
