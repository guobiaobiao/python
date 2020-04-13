import requests
from common.commonDate import CommonDate

class HttpUtil:
    def __init__(self):
        self.http=requests.session()
        self.headers={'Content-Type':'application/json; charset=utf-8'}

    def post(self,path,date):
        host=CommonDate.host #获取全局变量host路径
        url = host + path
        resp=self.http.post(url,data=date,headers=self.headers)
        assert resp.status_code==200
        return  resp

    def get(self,path):
        host=CommonDate.host
        url = host + path
        resp = self.http.get(url)
        assert resp.status_code == 200
        return resp

