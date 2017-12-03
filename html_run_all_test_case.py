import os
import smtplib
import unittest
# HTMLTestRunner.py是基于unittest框架的一个扩展，可以在网上自行下载
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    f = open(path, 'rb')
    mail_body = f.read()
    f.close()

    # 要想发邮件，需要把二进制的内容转成MIME格式
    # MIME multipurse多用途 ，Internet 互联网 ,Mail 邮件，Extension 扩展
    # MIME是对邮件协议的一个扩展，是邮件不仅支持文本，还支持多种格式，比如：图片，音频，二进制文件等
    msg = MIMEText(mail_body,'html','utf-8')
    # 上面是邮件的正文，还应有主题，发件人，收件人
    # msg是字典类型
    msg['Subject'] = Header('自动化测试报告','utf-8')
    # 如果想用客户端软件或者自己写代码登录邮箱，很多类型的邮件，需要单独设置一个客户端授权码
    msg['From'] = 'bwftest126@126.com'
    msg['To'] = 'qiwenyanzi@163.com'

    # 以上 邮件内容已经准备好了
    # 发邮件的手动步骤
    # 1.打开邮箱登录页面 连接邮箱服务器
    # 要想连接服务器，首先需搞清楚网络传输协议
    # 发邮件的协议，一般有三种协议，查看邮箱支持哪种协议
    # pop3,smtp,imap
    # 从中选择一种传输协议，用例发邮件，我们选择smtp
    # smtp 简单邮件传输协议
    # 首先导入smtolib.SMTP的代码库
    smtp= smtplib.SMTP() # 实例化一个SMTP类的对象
    smtp.connect('smtp.126.com') # 连接126邮箱的服务器地址

    # 2.输入用户名密码登录
    smtp.login('bwftest126@126.com','abc123asd654')
    # 3.发送邮件
    smtp.sendmail(msg['From'],  msg['To'] , msg.as_string())
    # 4.退出邮箱
    smtp.quit()
    print('email has sent out!')





if __name__ == '__main__':
    # str --> String f -->format格式
    # strftime() 通过这个方法可以定义时间的格式
    now = time.strftime("%Y-%m-%d_%H-%M-%S")


    suit = unittest.defaultTestLoader.discover('./day5','*test.py')
    # unittest.TextTestRunner().run(suit) 文本测试用例运行器
    # html的测试用例运行器
    # html的测试用例运行器最终会生成一个html格式的测试报告
    base_path = os.path.dirname(__file__)
    path = base_path + '/report/repot'+now +'.html'
    # file = open('./report/repot'+ now + '.html' ,'wb')
    file = open(path ,'wb')
    # stream=sys.stdout 系统标准输出 二进制输出 title=None, description=None
    HTMLTestRunner(stream=file, title='海盗商城测试报告', description="测试环境：Windows Server 2008 + Chrome").run(suit)
    file.close()
    send_mail(path)
    # 新的测试报告会覆盖原来的测试报告
    # 加一个时间戳
    # 发邮件