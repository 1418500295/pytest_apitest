import os
import pytest
import requests
from utils.run_main import RunMain
from utils.operate_yaml import OperateYaml
from utils.operate_json import OperateJson
from utils.fileconfig import FileConfig
from config.operate_logging import LogConfig

logger = LogConfig.get_logger()
class TestFirst():
    """
    初始化操作
    function 表示每个函数运行前后调用，yield之前做setup操作，yield之后做teardowm操作
    class每个测试类运行前后做一次
    """
    @pytest.fixture(scope='function',autouse=True)
    def simple_setup(self):
        print("测试开始")
        yield
        print("测试结束")

    def test_01(self):
        data = OperateJson.get_json("getDemo.json")
        rs = RunMain.get_main(FileConfig.get_url("getDemo"),params=data)
        logger.info("实际结果是{}".format(rs))


    def test_02(self):
        rs = requests.get(url=FileConfig.get_url("getCookies"),params='')
        print(rs.text)
        print(rs.cookies)
        for k,v in rs.cookies.items():
            print(k,v)
        return rs.cookies

    def test_03(self):
        rs = requests.get(url=FileConfig.get_url("getwithcookies"),cookies= TestFirst().test_02())
        print(rs.text)


if __name__ == '__main__':
    pytest.main(['-s','-q'])
    # print(os.path.dirname(os.getcwd()))

