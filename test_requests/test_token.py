import pytest
import requests


class TestToken:
    @pytest.mark.parametrize(
        "corp_id, corp_secret, errmsg",[("ww32f831277a3c395f", "9n1UoQkHZCXtaOyrK0cXVFYXHsUH2jCoigaMfNSWps4", "ok"),
                                ("ww32f831277a3c395f", "", "corpsecret missing"),
                                ("", "9n1UoQkHZCXtaOyrK0cXVFYXHsUH2jCoigaMfNSWps4", "corpid missing")],
        ids = ['correct', 'missing secret', 'missing id']
    )
    def test_get_token(self, corp_id, corp_secret, errmsg):
        # corpid = "ww32f831277a3c395f"
        # corpsecret = "9n1UoQkHZCXtaOyrK0cXVFYXHsUH2jCoigaMfNSWps4"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        r = requests.get(url)
        assert r.json()["errmsg"] == errmsg

    @pytest.mark.parametrize(
        "corp_id, corp_secret, errmsg", [("ww32f831277a3c395f", "9n1UoQkHZCXtaOyrK0cXVFYXHsUH2jCoigaMfNSWps4", "ok"),
                                         ("ww32f831277a3c395f", "", "corpsecret missing"),
                                         ("", "9n1UoQkHZCXtaOyrK0cXVFYXHsUH2jCoigaMfNSWps4", "corpid missing")],
        ids=['correct', 'missing secret', 'missing id']
    )
    def test_token_param(self, corp_id, corp_secret, errmsg):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url,params={"corpid": corp_id, "corpsecret": corp_secret})
        assert r.json()["errmsg"] == errmsg
        self.access_token = r.json()['access_token']