# coding:utf-8
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf8')

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d%H%H%S")
    filename = './report/' + now + '_restult.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()
