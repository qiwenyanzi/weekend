import time

from day5.my_test_case import MyTestCase
from day6.database.connect_db import connect_db


class ZhuceTest(MyTestCase):
    def test_zhuce(self):
        driver = self.driver
        driver.get('http://localhost/index.php?m=user&c=public&a=reg')
        driver.find_element_by_name('username').send_keys('ceshi10')
        driver.find_element_by_name('password').send_keys('123456')
        driver.find_element_by_name('userpassword2').send_keys('123456')
        driver.find_element_by_name('mobile_phone').send_keys('13689945612')
        driver.find_element_by_name('email').send_keys('ceshi10@163.com')
        driver.find_element_by_class_name('reg_btn').click()
        # 检查数据库中新增的记录的用户名和我们输入的用户名是否一致
        expected = 'ceshi10'
        time.sleep(3)
        actual = connect_db()[1]
        self.assertEqual(expected,actual)