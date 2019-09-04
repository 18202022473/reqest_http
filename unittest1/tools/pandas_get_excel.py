import pandas as pd
from lemon.unittest1.tools.project_path import *

df = pd.read_excel(excel_path)
test_data = []
for i in df.index:
    row_data = df.loc[i, ['url', 'requests_data', 'method', 'case_id']].to_dict()
    test_data.append(row_data)
print(f'最后获取到的数据是{test_data}')
