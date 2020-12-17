import requests
from jsonpath import jsonpath
from jsonschema import validate


class BaseApi:

    def send_requests(self, req:dict):
        # 对request进行二次封装
        # req = {
        #     "method": "get",
        #     "url": "XXXX",
        #     "params": {},
        #     "json": {}
        # }
        return requests.request(**req)

    def base_jsonpath(self, obj, json_exp):
        return jsonpath(obj, json_exp)

    def base_jsonschema(self, re, schema):
        return validate(re, schema)