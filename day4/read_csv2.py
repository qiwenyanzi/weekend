# 1.read_csv.py不能被其他测试用例调用，需封装到一个方法里
# 2.每个测试用例的路径不同，所以path不能写死，应该作为参数传入到这个方法中
# 4.文件打开，没有关闭，最终造成内存泄露
import csv
import os

# 打开关闭浏览器也可以使用with...as..，但是我们采用setup和teardown
# try...finally..也可以保证中间发生异常，文件最后也可以关闭，但是这种语法可读性比较差
def read(file_name):
    # 所以的重复的代码的出现，都是程序设计的不合理
    # 重复的代码都封装称方法
    base_path = os.path.dirname(__file__)
    path = base_path.replace('day4', 'data/'+file_name)
    #file = open(path,'r')
    # with代码块可以自动关闭with中声明的变量file
    result = []
    with open(path,'r') as file:
        data_table = csv.reader(file)
        for row in data_table:
            # print(row)
            result.append(row)
    return result

    # 3 关闭
    # 如果在打开和关闭程序的代码中间发生了异常，导致后面的代码不能正常运行
    # 导致文件不能关闭
    # 应该使用with...as..语句实现文件的关闭

        #file.close()

if __name__ == '__main__':
    #path = r'C:\Users\51Testing\PycharmProjects\weekend\data\menmber_info.csv'
    # 3.这个路径是绝对路径
    # __file__是python内置的变量，指的是当前文件
    # base_path = os.path.dirname(__file__)
    # path = base_path.replace('day4','data/menmber_info.csv')
   # print(path)
    member_info =read("menmber_info.csv")
    for row in member_info:
        print(row)
    # 5.读出数据不是目的，目的是通过数据驱动测试，所以应该把数据作为方法的返回值返回
    #print(member_info)
