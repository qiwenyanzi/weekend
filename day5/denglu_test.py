import unittest

import time
from selenium import webdriver


class DengLuTest(unittest.TestCase):
    """登录模块测试用例"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

    def test_denglu(self):
        """登录测试正常情况测试用例"""
        driver = self.driver
        driver.get('http://localhost/index.php?m=user&c=public&a=login')
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys('ceshi1')
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys('123456')
        driver.find_element_by_class_name('login_btn').click()