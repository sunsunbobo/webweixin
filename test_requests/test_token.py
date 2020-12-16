import requests


class TestToken:
    def test_get_token(self):
        # 获取access token
        # ww32f831277a3c395f
        # 9n1UoQkHZCXtaOyrK0cXVFYXHsUH2jCoigaMfNSWps4
        corpid = "ww32f831277a3c395f"
        corpsecret = "9n1UoQkHZCXtaOyrK0cXVFYXHsUH2jCoigaMfNSWps4"

        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url)
        print(r.status_code)
        print(r.json())
        access_token = r.json()['access_token']
        print(access_token)

    def test_token_param(self):
        corpid = "ww32f831277a3c395f"
        corpsecret = "9n1UoQkHZCXtaOyrK0cXVFYXHsUH2jCoigaMfNSWps4"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url,params={"corpid":corpid, "corpsecret":corpsecret})
        print(r.status_code)
        print(r.json())
        access_token = r.json()['access_token']
        print(access_token)