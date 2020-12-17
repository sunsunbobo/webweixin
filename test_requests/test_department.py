import requests


class TestDepartments:
    def setup_class(self):
        corpid = "ww32f831277a3c395f"
        corpsecret = "9n1UoQkHZCXtaOyrK0cXVFYXHsUH2jCoigaMfNSWps4"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url, params={"corpid": corpid, "corpsecret": corpsecret})
        print(r.status_code)
        print(r.json())
        self.access_token = r.json()['access_token']
        print(self.access_token)
        self.id = 2

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
           "id": self.id
        }
        r = requests.post(url, json=data, params=param)
        print(r.status_code)
        print(r.json())
        assert r.json()['errcode'] == 0 and r.json()['errmsg'] == "created"
        get_list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        r1 = requests.get(get_list_url, params=param)
        assert r1.json()['department'][1]['name'] == '广州研发中心'

    def test_update_department(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        param = {
            "access_token": self.access_token
        }
        data = {
            "name": "技术部",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": self.id
        }
        r = requests.post(url, json=data, params=param)
        print(r.status_code)
        print(r.json())
        assert r.json()['errcode'] == 0 and r.json()['errmsg'] == "updated"
        get_list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        r1 = requests.get(get_list_url, params=param)
        assert r1.json()['department'][1]['name'] == '技术部'


    def test_delete_department(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        param = {
            "access_token": self.access_token,
            "id": self.id
        }
        r = requests.get(url, params=param)
        print(r.status_code)
        print(r.json())
        assert r.json()['errcode'] == 0 and r.json()['errmsg'] == "deleted"


    def test_get_department(self):
        get_list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        param = {
            "access_token": self.access_token
        }
        r1 = requests.get(get_list_url, params=param)
        assert r1.json()['department'][1]['name'] == '技术部'