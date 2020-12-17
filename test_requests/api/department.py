import requests

from test_requests.api.wework import WeWork


class Department(WeWork):
    def create_department(self, department_id):
        req = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}",
            "json": {
                "name": "广州研发中心",
                "name_en": "RDGZ",
                "parentid": 1,
                "order": 1,
                "id": department_id
            }
        }
        r = self.send_requests(req)
        return r.json()

    def update_department(self, department_id):
        req = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}",
            "json": {
                "name": "技术部",
                "name_en": "RDGZ",
                "parentid": 1,
                "order": 1,
                "id": department_id
            }
        }
        r = self.send_requests(req)
        return r.json()

    def delete_department(self, department_id):
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={department_id}"
        }
        r = self.send_requests(req)
        return r.json()

    def get_department_list(self):
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        }
        r1 = self.send_requests(req)
        return r1.json()