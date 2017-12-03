# 要读csv文件，需首先准备一个csv文件
# 1.导入csv包 csv是python语言内置的包
import csv
# 2.文件路径
# 三种方式：1.\-->\\ 2.\-->/ 3.在字符传前添加r ,表示反斜杠是普通字符，不看着转义字符
path = r'C:\Users\51Testing\PycharmProjects\weekend\data\menmber_info.csv'
# 3.通过路径打开文件
file = open(path,'r')
# 4.通过csv代码库，读取csv格式文件的内容
data_table = csv.reader(file)
# 5.遍历data_table,分别打印每行数据
for row in data_table:
    print(row)
