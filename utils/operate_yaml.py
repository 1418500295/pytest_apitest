import os

import yaml
class OperateYaml():
    @staticmethod
    def get_yaml(file_name):
        try:
            project_path = os.path.dirname(os.getcwd())
            yaml_file = project_path + "/" + file_name
            with open(yaml_file,"r",encoding="utf-8")as f:
                data = yaml.load(f,Loader=yaml.FullLoader)

                return data
        except FileNotFoundError as e:
            print("{} not found".format(e))



if __name__ == '__main__':
    print(OperateYaml.get_yaml("config.yaml"))
