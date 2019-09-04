import os
project_path = os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]
excel_path = os.path.join(project_path, 'unittest1', 'file', 'case_data.xlsx')
config_path = os.path.join(project_path, 'unittest1', 'file', 'config.txt')
test_html_path = os.path.join(project_path, 'unittest1', 'file', 'test.html')
log_path = os.path.join(project_path, 'unittest1', 'tools', 'py12.txt')

