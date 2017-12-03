# 1.登录
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://localhost/index.php?m=user&c=public&a=login')
driver.implicitly_wait(30)
driver.maximize_window()
driver.find_element_by_id('username').send_keys('ceshi')
# driver.find_element_by_id('username').send_keys(Keys.TAB)
# Chains链表和数组不同，数组有固定得长度，链表必须得有明确的结尾
ActionChains(driver).send_keys(Keys.TAB).send_keys('123456').send_keys(Keys.ENTER).perform()
# 2.点击账号设置
driver.find_element_by_link_text('账号设置').click()
# 3.点击个人资料
driver.find_element_by_partial_link_text('个人资料').click()
# 4.修改个人信息
# 更好的编程习惯，在执行sendkeys之前，都执行一下clear
driver.find_element_by_id('true_name').clear()
driver.find_element_by_id('true_name').send_keys('测试一')
# css可以用多个属性定位一个元素
# 一个元素的多个属性之前不能有空格
driver.find_element_by_css_selector('[value="2"]').click() # 可以组合'#xb[value="2"]'

# 元素定位和元素操作
js = 'document.getElementById("date").removeAttribute("readonly")'
driver.execute_script(js)
driver.find_element_by_id('date').clear()
driver.find_element_by_id('date').send_keys('1990-01-05')
# 使用arguments 用selenium的定位方式，定位元素后对元素执行js脚本，删除readonly属性
# data = driver.find_element_by_id('date')
# driver.execute_script('argumets[0].removeAttribute("readonly")',data)
# data.clear()
# data.send_keys('1990-01-01')
# 用selenium调用js 一共有两个关键字：
# 1.argument[0]:用python语言代替一部分javascript
# 好处是：有时selenium定位比较容易
# 2.return 把javascript的执行结果返回给python
# 好处：有时selenium定位不到的元素，我们可以用js定位到
# date = driver.execute_script("return document.getElementById('data')") # 用于元素定位
# # 这句话 == data = driver.find_element_by_id('date')

driver.find_element_by_id('qq').clear()
driver.find_element_by_id('qq').send_keys('812789456')
driver.find_element_by_class_name('btn4').click()
# 右键检查不了html代码的弹窗口，叫alert
# alert控件不是html代码生产的，所以implicitly_wait对这个控件
time.sleep(3)
driver.switch_to.alert.dismiss() # accept（）
