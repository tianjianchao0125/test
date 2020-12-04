import os
import time
import unittest

from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':

    # 1、找出所需执行的测试用例，TestLoader执行测试用例的加载器
    test_dir = './testcase'
    discover = unittest.defaultTestLoader.discover(start_dir='./testcase',pattern='test*.py')

    # 2-1、通过unittest执行测试用例集
    # unittest.TextTestRunner().run(suite)
    # 2-2、通过HTMLTestRunner文件执行测试用例集
    file_path = os.path.dirname(__file__)  # 先找到本文件的路径
    # 获取时间戳
    time_stamp = time.strftime('%Y%m%d_%H-%M-%S')  # strftime
    # 先找到本文件 放到report下面 加上文件名  加上时间戳
    all_path = file_path + "/report/" + "招聘小程序测试报告" + time_stamp + ".html"
    # w写 b二进制
    file = open(all_path, 'wb')
    HTMLTestRunner(stream=file, verbosity=1, title='小程序招聘自动化测试报告',
                    description='测试环境：win10、i7、8G、SSD500G',).run(discover)
    # BSTestRunner(stream=file,verbosity=1,title='1910自动化测试报告',
    #                description='测试环境：win10、i7、8G、SSD500G', tester = '田建朝').run(suite)
    file.close()  # 关闭文件

