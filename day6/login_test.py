import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.my_test_case import MyTestCase
from day6.page_object.login_page import LoginPage
from day6.page_object.pesonal_center_page import PesonalCenterPage


class LoginTest(MyTestCase):
    def test_login(self):
        # 这种测试用例可读性比较差，维护起来比较困难
        # 那么测试用例写成什么样可读性比较好呢
        # 1.打开网页
        self.driver.get('http://localhost/index.php?m=user&c=public&a=login')
        lp = LoginPage(self.driver) # 实例化一个登录页面
        # 2.输入用户名
        #self.driver.find_element(By.ID,'username').send_keys('ceshi1')
        lp.input_username('ceshi1')
        # 3.输入密码
        #self.driver.find_element(By.ID,'password').send_keys('123456')
        lp.input_password('123456')
        # 4.点击登录按钮
        #self.driver.find_element(By.CLASS_NAME,'login_btn').click()
        lp.click_login_button()
        # 5.验证是否跳转到管理中心页面
        expeced = '我的会员中心 - 道e坊商城 - Powered by Haidao'
        # time.sleep(2)
        # self.assertIn('我的会员中心',self.driver.title)
        pcp = PesonalCenterPage(self.driver)
        time.sleep(2)
        self.assertEqual(pcp.title,self.driver.title)