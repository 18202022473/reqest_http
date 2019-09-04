import unittest
import HTMLTestRunnerNew
from lemon.unittest1.class_01.request_http import RequestsAPI
from lemon.unittest1.tools.project_path import *

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(RequestsAPI))
with open(test_html_path, 'wb')as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='性能测试报告', description='关于系统稳定性',
                                              tester='Marico')
    runner.run(suite)
