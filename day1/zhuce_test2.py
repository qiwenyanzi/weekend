# 1.打开浏览器
from  selenium import webdriver
driver = webdriver.Chrome()
# 2.打开商城主页(网址必须包含协议信息)
driver.get('http://localhost/')
# 3.点击注册连接
# 第四种元素定位方式：链接的文本信息
driver.find_element_by_link_text('注册').click()

# ***** 窗口切换：把selenium切换到新的窗口工作 *****
cwh = driver.current_window_handle # 浏览器当前窗口的句柄
print(cwh) # CDwindow-ee0f3566-234c-43e1-852d-f7f6b8a13bcc
whs = driver.window_handles # 浏览器中所有的窗口句柄
print(whs) # ['CDwindow-ee0f3566-234c-43e1-852d-f7f6b8a13bcc', 'CDwindow-61635b36-8e48-4c83-a2d0-bc4072593e0a']
for item in whs:
    if item == cwh:
        driver.close()
    else:
        driver.switch_to.window(item)
# 4.输入用户信息
#driver.find_element_by_name('keyword').send_keys('123456')
driver.find_element_by_name('username').send_keys('ceshi2')
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_name('userpassword2').send_keys('123456')
driver.find_element_by_name('mobile_phone').send_keys('13678945622')
driver.find_element_by_name('email').send_keys('ceshi2@163.com')
# 5.点击提交按钮
driver.find_element_by_class_name('reg_btn').click()