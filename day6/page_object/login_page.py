from selenium.webdriver.common.by import By


class LoginPage:
    # 构造方法的作用 ：实例化LoginPage对象
    # 实例化LoginPage对象的时候，必须要调用构造方法
    # 需要把driver作为参数传进来
    # 便于别的属性和方法是使用driver
    def __init__(self,driver): # driver是从login_test.py传过来的
        self.driver = driver

    # 属性
    title = '用户登录 - 道e坊商城 - Powered by Haidao'
    url = 'http://localhost/index.php?m=user&c=public&a=login'
    # 元组，元组中有两个元素，第一个元素是控件的定位方式，第二个元素是控件具体的值
    username_input_loc = (By.ID,'username')
    password_input_loc = (By.ID,'password')
    login_button_loc = (By.CLASS_NAME, 'login_btn')

    # 方法
    def open(self):
        self.driver.get(self.url)
    def input_username(self,username):
        # self.driver.find_element_by_id('username').send_keys(username)
        #self.driver.find_element(By.ID,'username').send_keys(username
        # *表示传入的就不是元组，而是元组中的两个元素
        self.driver.find_element(*self.username_input_loc).send_keys(username)
    def input_password(self,password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)
    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc ).click()