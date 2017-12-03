import unittest

if __name__ == '__main__':
    # defaultTestLoader 默认的测试用例加载器，用于寻找符合一定规则的测试用例
    # suit 表示一组测试用例，一般用suit表示
    suit = unittest.defaultTestLoader.discover('./day5', pattern='*test.py')
    # 执行suite中所有的测试用例
    # TextTestRunner 文本测试用例运行器
    # unittest.TextTestRunner.run(suit) ---> TextTestRunner首字母大写，说明它是一个类，类不能直接调用方法
    # 必须要实例化对象才能调用方法
    # python中实例化不需要new关键字，直接在类名后加（）就可以了
    unittest.TextTestRunner().run(suit)