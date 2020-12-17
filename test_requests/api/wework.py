from test_requests.api.baseapi import BaseApi


class WeWork(BaseApi):
    def get_token(self, corp_secret):
        corp_id = "ww32f831277a3c395f"
        # corp_secret = "9n1UoQkHZCXtaOyrK0cXVFYXHsUH2jCoigaMfNSWps4"
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        }
        r = self.send_requests(req)
        self.token = r.json()['access_token']
        return self.token