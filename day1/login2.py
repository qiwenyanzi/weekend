# 1.打开浏览器
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://localhost/')
# 2.点击登录链接

# ****** 窗口切换的第一种方法：
# whs = driver.window_handles
# cwh = driver.current_window_handle
# for item in whs:
#     if item == cwh:
#         driver.close()
#     else:
#         driver.switch_to.window(item)

# ******* 窗口切换的第二种方法：

# javascript
# 学好selenium，最重要的三件事：
# 1.元素定位:id-->name-->class link_text:必须是链接，必须是a标签，必须是文本
# 2.元素的操作：鼠标左键单击click
# 3.javascript
# 在python中运行javascript
js ='document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
driver.execute_script(js)

driver.find_element_by_link_text('登录').click()


# 3.输入用户名
driver.find_element_by_id('username').send_keys('ceshi1')
# 4.输入密码
driver.find_element_by_id('password').send_keys('123456')
# 5.点击登录按钮
driver.find_element_by_class_name('login_btn').click()

