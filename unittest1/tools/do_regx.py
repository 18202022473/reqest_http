import re
from lemon.unittest1.tools.get_data import GetData


# 第一种方式(头部匹配)：
# s = 'www.lemfix.com'
# res = re.match('(w)(ww)', s)
# print(res.group())  # 与group(0)结果一致
# print(res.group(0))
# print(res.group(1))
# print(res.group(2))
# 第二种方式：
# 在字符串里找，匹配的内容存在字符串中
# s = 'hellolemonfixlemon'
# res = re.findall('(le)(mon)', s)  # 有分组以列表嵌套元组形式表现
# res1 = re.findall('lemon', s)
# print(res)
# print(res1)
# 第三种方式：
# (单次匹配)
# s = "{'password': 'af8f9dffa5d420fbc249141645b962', 'phone': '${phone}', 'verificationCode': '123'}"
# res = re.search("\${(.*?)}", s)
# print(res)
# print(res.group(0))
# print(res.group(1))
# (多次匹配)
class DoRegx:
    @staticmethod
    def do_regx(s):
        while re.search("\${(.*?)}", s):
            rg = re.search("\${(.*?)}", s)
            key = rg.group(0)
            value = rg.group(1)
            s = s.replace(key, str(getattr(GetData, value)))
            # print(key, value)
            # print(s)
        return s


if __name__ == '__main__':
    s = "{'password': '${password}', 'phone': '${phone}', 'verificationCode': '123'}"
    res = DoRegx.do_regx(s)
    print(res)
