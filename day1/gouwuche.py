# 登录--->回商城主页--->搜索--->把商品加入购物
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://localhost/")
# js = 'document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
# driver.execute_script(js)
driver.find_element_by_link_text('登录').click()
for item in driver.window_handles:
    if item != driver.current_window_handle:
        driver.switch_to.window(item)


driver.find_element_by_id('username').send_keys('ceshi')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_class_name('login_btn').click()

driver.find_element_by_link_text('进入商城购物').click()
driver.find_element_by_name('keyword').send_keys('iphone')
driver.find_element_by_class_name('btn1').click()

js1 = 'document.getElementsByClassName("shop_01-imgbox")[0].childNodes[1].removeAttribute("target")'
driver.execute_script(js1)
driver.find_element_by_css_selector('body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a > img').click()
driver.find_element_by_id('joinCarButton').click()

driver.find_element_by_class_name('shopCar_T_span3').click()
driver.find_element_by_link_text('结算').click()