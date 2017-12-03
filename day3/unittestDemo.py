# 测试框架
# 最主要的用途是组织和执行测试用例
# 1.导入unittest
import unittest

# java中类名和文件名的关系：public的类名和文件名一样
# python中的可以一样，但是推荐：文件名首字母小写，类名首字母大写

# 2.继承unittest中的父类
class UnittestDemo(unittest.TestCase):
    # 3.重写父类中的方法 setUp和tearDown
    def setUp(self):
        print('这个方法将在测试用例执行之前先执行')

    def tearDown(self):
        print('这个方法将会在测试用来执行之后执行')
# 4.编写测试用例方法
    # 只有以test开头命名的方法才是测试用例方法
    # 测试用例方法可以直接被运行，普通方法不能直接运行，只有被调用才能执行
    def test_login(self):
        print('登录测试用例')
        self.zhuce()

    def zhuce(self):
        print("注册测试用例")

    def test_search(self):
        print("搜索测试用例")
# 如果你直接执行这个文件，那么就会执行下面的语句
# 否则你执行其他文件，import这个文件的时候，下面的代码就不执行
if __name__ == '__main__':
    # 执行当前文件中所有的unittest的测试用例
    unittest.main()


