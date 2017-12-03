# 1.打开浏览器
from selenium import webdriver
# 从selenium  导入 网络驱动
driver = webdriver.Chrome()
# 2.打开登录页
driver.get('http://localhost/index.php?m=user&c=public&a=login')
# 3.输入用户名
driver.find_element_by_id('username').send_keys('ceshi1'.strip())
# 4.输入密码
driver.find_element_by_id('password').send_keys('123456')
# 5.点击登录按钮
driver.find_element_by_class_name('login_btn').click()
# driver.find_element_by_class_name('login_btn fl').click()  # invalid selector: Compound class names not permitted