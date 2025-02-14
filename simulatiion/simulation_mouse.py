#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys  # 引入keys类操作
import time

def s(int):
    time.sleep(int)

chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.get('http://www.baidu.com')
print '现在将浏览器最大化'
browser.maximize_window()
text = browser.find_element_by_name('tj_trnews').text
print text  # 打印备案信息

browser.find_element_by_id('kw').send_keys(u'郭世杰')
print browser.find_element_by_id('kw').get_attribute('type')
print browser.find_element_by_id('kw').size #打印输入框的大小
browser.find_element_by_id('su').click()
time.sleep(1)

print '现在我将设置浏览器为宽480，高800显示'
browser.set_window_size(480,800)
browser.get('http://m.mail.10086.cn')
time.sleep(1)

print '现在我将回到刚才的页面'
browser.maximize_window()
browser.back()
time.sleep(1)

# print '现在我将回到之前的页面'
# browser.forward()
# time.sleep(5)
# print '现在我将打开杨彦星的网站进行json搜索'
# browser.get('http://www.yangyanxing.com')
# browser.find_element_by_xpath(".//*[@id='ls']").send_keys(u'json')
# browser.find_element_by_xpath(".//*[@id='header']/div[1]/div/form/input[2]").click()
# time.sleep(5)
# browser.quit()

# browser = webdriver.Chrome()

print '以下将以登录人人网来进行上面的综合应用'
browser.get('http://www.renren.com/SysHome.do')
browser.find_element_by_id('email').clear()  # 这个是以id选择元素
browser.find_element_by_id('email').send_keys('guoshijie_hi@yeah.net')
browser.find_element_by_id('email').send_keys(Keys.BACK_SPACE)
time.sleep(1)
browser.find_element_by_id('email').send_keys('t')
s(1)
browser.find_element_by_id('email').send_keys(Keys.CONTROL, 'a')  # 全选
s(1)
browser.find_element_by_id('email').send_keys(Keys.CONTROL, 'x')  # 剪切掉里面的内容
s(1)
browser.find_element_by_id('email').send_keys(Keys.CONTROL, 'v')  # 重新输入进去
s(1)
browser.find_element_by_name('password').clear()  # 这个是以name选择元素
browser.find_element_by_name('password').send_keys('guoyanjie')
# browser.find_element_by_xpath(".//*[@id='login']").click()#这个是以xpath选择元素
browser.find_element_by_xpath(".//*[@id='login']").send_keys(Keys.ENTER)  # 这里通过点击Enter键来登录
browser.maximize_window()
s(1)
article = browser.find_element_by_link_text(u'郭鹏波')
ActionChains(browser).move_to_element(article).perform()  # 将鼠标移动到这里，但是这里不好用
ActionChains(browser).click(article).perform()
# ActionChains(browser).context_click(article).perform()
time.sleep(3)

browser.quit()



