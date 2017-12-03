import time


from selenium import webdriver

# 45版本以下的firefox浏览器，不需要驱动文件
# 从46版本以上的，需要把driver.exe放到环境变量下？？？
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# 隐式等待 在创建浏览器时设置
driver.implicitly_wait(30)
driver.maximize_window()

driver.get('http://localhost/')

# 在点击登录按钮之前，我们需要先删除target属性
# 用selenium的定位方式替换javascript的定位方式
# 需要用arguments关键字，可以把元素定位作为一个参数，替换到javascript语句中
login_link = driver.find_element_by_link_text('登录')
driver.execute_script('arguments[0].removeAttribute("target")', login_link)  # ？？格式化？？
login_link.click()
# driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
driver.find_element_by_id('username').send_keys('ceshi')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('password').submit()
# 不推荐使用 1.只能用于表单 但是click可以用于任何情况 2.不是模拟键盘操作
# submit()用于提交form表单。form是html中的一个元素
# from表单的任何子孙节点都可以调用submit()方法提交表单
# Alt+enter可以自动导包
# time.sleep(5)
# 使用隐式等待，会自动判断网页是否加载完毕，当加载完成立刻开始执行后续操作

driver.find_element_by_link_text('进入商城购物').click()
driver.find_element_by_name('keyword').send_keys('iphone')
driver.find_element_by_name('keyword').submit()

# img是标签名，> 标签前面是父节点，后面是子节点
# 如果想在css中写class属性，那么前面需要加上小数点
# iphone_image = 'body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img'
# iphone_link = 'body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a '
# # ：nth-child(2)表示当前节点是父亲的第二个儿子
# iphone_link2 =  'body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div：nth-child(2) > div.shop_01-imgbox > a '
# 将css_selector中的内容改短
# 因为涉及到的节点越多，那么代码的健壮性和可维护性越差。一旦开发修改页面时，修改了这些节点，那么元素定位失败
iphone_link3 = 'div.shop_01-imgbox > a '
iphone = driver.find_element_by_css_selector(iphone_link3)
driver.execute_script('arguments[0].removeAttribute("target")', iphone)
iphone.click()

driver.find_element_by_id('joinCarButton').click()
driver.find_element_by_class_name('shopCar_T_span3').click()
driver.find_element_by_class_name('shopCar_btn_03').click()

driver.find_element_by_class_name('add-address').click()
driver.find_element_by_name('address[address_name]').send_keys('ceshi')
driver.find_element_by_name('address[mobile]').send_keys('13678945612')
# driver.父节点.子节点.click()
# driver.find_element_by_id('add-new-area-select').find_element_by_css_selector('[value="230000"]').click()
# 子的value在页面上唯一 所以改为下面：
# driver.find_element_by_css_selector('[value="230000"]').click()
# driver.find_element_by_css_selector('[value="230500"]').click()
# driver.find_element_by_css_selector('[value="230506"]').click()
# driver.find_element_by_name('address[address]').send_keys('北京海淀迈行大厦')
# driver.find_element_by_name('address[zipcode]').send_keys('010010')
# driver.find_element_by_class_name('aui_state_highlight').click()

# 定位第一个下拉框
sheng = driver.find_element_by_id('add-new-area-select')

# 下拉框是一种比较特殊的网页元素，selenium专门为下拉框提供了一种定位方法
# 把sheng这个元素从webElement类型转换称Select类型
# Select是selenium专门为我们创建的一个类，用于操作下拉框
# Select这个类中封装了很多操作下拉框的方法

Select(sheng).select_by_value('230000')
# 定位第二个下拉框 动态的 id会变化
shi = driver.find_elements_by_tag_name('select')[1]
Select(shi).select_by_index('2')
# 定位第三个下拉框
qu = driver.find_elements_by_tag_name('select')[2]
Select(qu).select_by_visible_text('克东县')