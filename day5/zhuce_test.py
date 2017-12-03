import os

from selenium import webdriver

from day5.my_test_case import MyTestCase


class ZhuCeTest(MyTestCase):
    """注册模块测试用例"""
    def test_zhu_ce(self):
        """打开注册页面测试用例"""
        driver = self.driver
        driver.get('http://localhost/index.php?m=user&c=public&a=reg')
        # driver.current_url() # 用来获取当前浏览器中的网址
        actul = driver.title # 用来获取当前浏览器中的标签名
        expected = '用户注册 - 道e坊商城 - Powered by Haidao'
        base_path = os.path.dirname(__file__)
        print(base_path)
        path =base_path.replace('day5','report/image/')
        driver.get_screenshot_as_file(path + 'zhuce.png')
        self.assertEqual(actul,expected)
