from  utils.operate_yaml import OperateYaml
from io import StringIO
class FileConfig():

    @staticmethod
    def get_url(uri_name):
        yaml_data = OperateYaml.get_yaml("config.yaml")
        uri = yaml_data[uri_name]
        if not uri.startswith("/"):
            uri = "/" + uri
        else:
            uri = uri
        test_url = yaml_data["host"] + uri
        return test_url

if __name__ == '__main__':
    url = FileConfig.get_url("getDemo")
    print(url)


