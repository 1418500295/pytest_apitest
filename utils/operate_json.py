import json
import os


class OperateJson():

    @staticmethod
    def get_json(file_name):
        project_path = os.path.dirname(os.getcwd())
        file_path = project_path + "/testdata/" + file_name
        with open(file_path,"r",encoding="utf-8")as f:
            json_data = json.load(f)
            return json_data

if __name__ == '__main__':
    data = OperateJson.get_json("getDemo.json")
    print(data)
