import requests


class TestDepartments:
    def setup(self):
        corpid = "ww32f831277a3c395f"
        corpsecret = "9n1UoQkHZCXtaOyrK0cXVFYXHsUH2jCoigaMfNSWps4"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url, params={"corpid": corpid, "corpsecret": corpsecret})
        print(r.status_code)
        print(r.json())
        self.access_token = r.json()['access_token']
        print(self.access_token)

    def test_create_department(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        param = {
            "access_token": self.access_token
        }
        data = {
           "name": "广州研发中心",
           "name_en": "RDGZ",
           "parentid": 1,
           "order": 1,
           "id": 2
        }
        r = requests.post(url, json=data, params=param)
        print(r.status_code)
        print(r.json())
        assert r.json()['errcode'] == 0 and r.json()['errmsg'] == "created"