import yaml

from test_requests.api.department import Department


class TestDepartments():
    def setup_class(self):
        self.department = Department()
        config_info = yaml.safe_load(open("config.yaml"))
        self.department.get_token(config_info['secret']['corp_secret'])

    def test_create_department(self):
        self.department.create_department(3)
        list1 = self.department.get_department_list()
        assert '广州研发中心' in self.department.base_jsonpath(list1, "$..name")

    def test_update_department(self):
        self.department.update_department(3)
        list2 = self.department.get_department_list()
        assert '技术部' in self.department.base_jsonpath(list2, "$..name")

    def test_delete_department(self):
        re = self.department.delete_department(3)
        list3 = self.department.get_department_list()
        assert 3 not in self.department.base_jsonpath(list3, "$..id")
        assert re['errcode'] == 0 and re['errmsg'] == "deleted"

    def test_get_department(self):
        self.department.get_department_list()