import unittest
# 1.导入ddt代码库
import ddt

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from day4.read_csv2 import read

# 2.装饰这个类
@ddt.ddt
class MemberManageTest(unittest.TestCase):
    # 3.调用之前写好的read() 方法，获取配置文件中的数据
    member_info = read('menmber_info.csv')

    @classmethod #在当前类只执行一次
    def setUpClass(cls):
        print('在所有方法之前只执行一次')
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        print('在所以方法之后只执行一次')
        time.sleep(5)
        cls.driver.quit()

    # 按照名称顺序执行 先执行登录再执行添加会员

    def test_a_login(self):
        print('登录测试')
        driver = self.driver
        driver.get('http://localhost/admin.php')
        driver.find_element_by_name('username').clear()
        driver.find_element_by_name('username').send_keys('admin')
        ActionChains(driver).send_keys(Keys.TAB).send_keys('password').send_keys(Keys.TAB).send_keys('1234').send_keys(Keys.ENTER).perform()

    # python中集合前面的星号表示把集合中的所有元素拆开，一个一个写
    # list = ['小红'，'小明']
    # *list = '小红'，'小明'
    # 5.@ddt.data()测试数据来源于read()方法
    # 把数据表中的每一行传入方法，在方法声明中增加一个参数row
    @ddt.data(*member_info)
    def test_b_add_member(self,row):
        # 每组测试数据就是一条测试用例，每条测试用例应该是独立的，不能因为上一条测试用例执行失败导致下一条数据不能被正常执行，所以这里不推荐使用for循环
        # 应该用ddt装饰器，去修饰这个方法，达到每条测试用例独立执行的目的
        # ddt 是 数据驱动测试 data driver test
        # 4.注释到for循环，改变代码缩进，使方法中的代码比方法申明缩进4个空格，快捷键是shift+tab
        #for row in read('menmber_info.csv'):
        # print('添加会员')
        driver = self.driver
        driver.find_element_by_link_text('会员管理').click()
        driver.find_element_by_link_text('添加会员').click()
        # 切换到子框架
        #driver.switch_to.frame('mainFrame')
        # 如果frame没有name属性时，我们可以通过其他方式定位iframe标签，把定位好的页面元素传给driver.switch_to.frame(iframe_html)方法也可以实现frame切换
        iframe_css = '#mainFrame'
        iframe_html = driver.find_element_by_css_selector(iframe_css)
        driver.switch_to.frame(iframe_html)
        driver.find_element_by_name('username').send_keys(row[0])
        driver.find_element_by_name('mobile_phone').send_keys(row[1])
        # driver.find_element_by_css_selector('[value="1"]').click()
        #driver.find_element_by_css_selector('[value="'+row[2]+'"]').click()  # 字符串拼接 +
        driver.find_element_by_css_selector('[value="{0}"]'.format(row[2])).click()  # 格式化
        driver.find_element_by_id('birthday').send_keys(row[3])
        driver.find_element_by_name('email').send_keys(row[4])
        driver.find_element_by_name('qq').send_keys(row[5])
        driver.find_element_by_class_name('button_search').click()

        # 自动判断程序运行是否正确
        # actual实际结果，执行测试用例后，页面上实际显示的结果
        time.sleep(3)
        actual = driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").text
        # expected 期望结果，来自于手动测试用例，需求文档，配置文件
        expected = row[0]
        # 断言和 if...else 语句类似,是用来做判断的
        # if actual ==expected:
        #     print('pass')
        # else:
        #     print('fail')

        # 断言assert,断言是框架提供的，要调用断言，需加上self. 因为测试用例继承了框架中的TestCase类，也继承了这个类中的断言，所以我们可以直接用断言方法
        # 断言的特点：
        # 1.断言比较简介
        # 2.断言只关注错误的测试用例：只有断言出错的时候，才会打印信息，正确时没有任何信息提示
        # 3.断言报错时，后面的代码将不会执行（看上面）
        self.assertEqual(actual,expected)

        # 切换到父框架
        driver.switch_to.parent_frame()
        # 切换到网页的根节点
        #driver.switch_to.default_content() # 此处两句等价 如果是三级框架parent_frame()是父框架，default_content()是祖先框架









# 执行时需要放到程序外面 否则可能有的会不执行 或者加入下面这句
if __name__ == '__main__':
    unittest.main()