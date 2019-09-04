import unittest
import requests
from lemon.unittest1.tools import get_excel
from ddt import ddt, data, unpack
from lemon.unittest1.tools.get_data import GetData
from lemon.unittest1.tools.project_path import *
from lemon.unittest1.tools.my_log import Mylog
my_log = Mylog()


def requests_method(url, requests_data, method):
    if method == 'get':
        res = requests.get(url, requests_data)
    if method == 'post':
        res = requests.post(url, requests_data)
    return res


@ddt
class RequestsAPI(unittest.TestCase):
    @data(*get_excel.get_excel(excel_path))
    @unpack
    def test_requests_class(self, url, requests_data, method, case_id, case_name, case_sheet):
        my_log.info(f'这是关于{case_name}的测试用例')
        # if case_id == 1:
            # get_excel.do_excel(excel_path, case_sheet, 0, '接口返回数据', 7)
            # get_excel.do_excel(excel_path, case_sheet, 0, '测试结果是否通过', 8)
        result = 'False'
        requests_data = eval(requests_data)
        '''不是登录的接口通过反射获取token'''
        if 'login' not in url:
            requests_data['token'] = getattr(GetData, 'token')
        '''发送requests请求'''
        res = requests_method(url, requests_data, method)
        '''将测试结果写回Excel中'''
        # get_excel.do_excel(excel_path, case_sheet, case_id, str(res.json()), 7)
        '''断言'''
        try:
            self.assertEqual(0, res.json()['statusCode'])
            result = 'True'
        except BaseException as e:
            my_log.error(f'{case_name}出错了，错误信息是：{e}')
            my_log.info(f'返回的数据是：{res.json()}')
            raise
        # finally:
            # get_excel.do_excel(excel_path, case_sheet, case_id, result, 8)
        '''登录接口成功登录后获取token'''
        if 'login' in url and res.json()['statusCode'] == 0:
            setattr(GetData, 'token', res.json()['content']['token'])
            # print(getattr(GetToken, 'token'))


if __name__ == "__main__":
    unittest.main()
