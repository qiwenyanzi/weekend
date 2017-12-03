# 1.登录
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(30)
#driver.maximize_window()
driver.get('http://localhost/index.php?m=admin&c=public&a=login')
driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('userpass').send_keys('password')
# 万能钥匙1234
driver.find_element_by_name('userverify').send_keys('1234')
driver.find_element_by_class_name('Btn').click()
# 2.商品管理
driver.find_element_by_link_text('商品管理').click()
# 3.添加商品
driver.find_element_by_link_text('添加商品').click()
# 4.商品名称
# 有一种特殊的网页 ，例如在左边或者上边有一个导航条 此时需注意
# 可能是一个页面中嵌套多个页面
# 其中“商品管理”和“添加商品”属于页面根节点的网页
# 商品名称属于frame框架里的子网页
driver.switch_to.frame('mainFrame')


driver.find_element_by_name('name').send_keys('安卓')


# 5.商品分类
driver.find_element_by_id('1').click()
# driver.find_element_by_css_selector("[id='2']").click()
driver.find_element_by_id('2').click()
driver.find_element_by_id('6').click()
driver.find_element_by_id('7').click()
# driver.find_element_by_id('jiafen').click()
# 双击是特殊的元素操作，被封装到ActionChains这个类中  java封装到Action这个类中
ActionChains(driver).double_click(driver.find_element_by_id('7')).perform()
# ActionChains可以用来执行一组操作 最后用perform结尾
# ActionChains(driver).click(driver.find_element_by_id('6')).double_click(driver.find_element_by_id('7')).perform()
# 这个不行 单击6后 才会出现7 但是ActionChains是perform之后才会一起执行

# 6.商品品牌
# driver.find_element_by_css_selector('body > div.content > div.install.tabs.mt10 > dl > form > dd:nth-child(1) > ul > li:nth-child(3) > select > option:nth-child(2)').click()
# driver.find_element_by_css_selector('[value="1"]').click()
brand = driver.find_element_by_name('brand_id')
Select(brand).select_by_index(1)
# 点击商品图册
driver.find_element_by_link_text('商品图册').click()
# 有些页面控件是javascript在页面加载之后生成的
# implicitily_wait 是用来判断整个网页是否加载完毕
# 有时页面加载完，但是javascript的控件还没有创建好，所以需要time.sleep()提高程序的稳定性
time.sleep(2)
# driver.find_element_by_css_selector('#filePicker label').click()
# 真正负责上传文件的页面元素是<input type="file" name="file" class="webuploader-element-invisible" multiple="multiple" accept="image/*">
# webuploader-element-invisible不可见的
# 所以我们直接操作这个控件，这个控件是可以直接输入图片的路径的
driver.find_element_by_name('file').send_keys('D:/123.png')
# 点击开始上传，同时用三个class定位
driver.find_element_by_css_selector('.uploadBtn.state-finish.state-ready').click()
time.sleep(3)
driver.switch_to.alert.accept()

# 页面太长点击不了下面的按钮 操作滚动条
# ac =  ActionChains(driver)
# for i in range(10):
#     ac.send_keys(Keys.ARROW_DOWN)
# ac.perform()

driver.execute_script('window.scrollTo(200,100)')
# 7.提交
driver.find_element_by_class_name('button_search').click()