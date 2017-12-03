import unittest

import time
from selenium import webdriver


class MemberManageTest(unittest.TestCase):
    # 变量前面加上self,表示这个变量是类的属性，可以被所有的方法访问
    def setUp(self):
        # driver声明在setUp方法只能，不能被其他方法访问
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        # quit 退出整个浏览器
        # close() 关闭一个浏览器
        # 代码编写和调试的时候需要在quit方法前加一个时间等待
        # 正式运行时去掉时间等待
        time.sleep(20)
        self.driver.quit()

    def test_add_menber(self):
        driver = self.driver
        driver.get('http://localhost/index.php?m=admin&c=public&a=login')
        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys('admin')
        driver.find_element_by_name('userpass').clear()
        driver.find_element_by_name('userpass').send_keys('password')
        driver.find_element_by_name('userverify').send_keys('1234')
        driver.find_element_by_name('userverify').submit()

        driver.find_element_by_link_text('会员管理').click()
        driver.find_element_by_link_text('添加会员').click()
        driver.switch_to.frame('mainFrame')

        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys('ceshi')

        driver.find_element_by_name('mobile_phone').clear()
        driver.find_element_by_name('mobile_phone').send_keys('1367894561')

        driver.find_element_by_css_selector('[value="0"]').click()

        driver.find_element_by_id('birthday').clear()
        driver.find_element_by_id('birthday').send_keys('2015-01-28')

        driver.find_element_by_name('email').clear()
        driver.find_element_by_name('email').send_keys('812978451@qq.com')
        driver.find_element_by_name('qq').clear()
        driver.find_element_by_name('qq').send_keys('812978451')
        driver.find_element_by_class_name('button_search').click()
# 类名需要大写, 或者两个单词之间没有空格,下划线, 单词的首字母大写, 或者首字母缩略词可以大写



