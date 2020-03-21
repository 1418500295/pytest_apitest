import pytest
import os
project_path = os.path.dirname(os.getcwd())
target_path = project_path + '/cases/'
if __name__ == '__main__':
    pytest.main(['-s','-q',target_path,'--alluredir','../report/data'])
    command = 'allure generate ../report/data -o ../report/html --clean'
    os.system(command)

