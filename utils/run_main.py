import requests

class RunMain():

    @staticmethod
    def get_main(url,params,headers=None):
        res = None
        try:
            if headers:
                res = requests.get(url=url,params=params,headers=headers).json()
            else:
                res = requests.get(url=url,params=params).json()
        except RuntimeError as e:
            print("{} is error".format(e))
        return res

    @staticmethod
    def post_main(url,data,headers=None):
        res = None
        try:
            if headers:
                res = requests.post(url=url,data=data,headers=headers).json()
            else:
                res = requests.post(url=url,data=data).json()
        except RuntimeError as e:
            print("{} is error".format(e))
        return res



