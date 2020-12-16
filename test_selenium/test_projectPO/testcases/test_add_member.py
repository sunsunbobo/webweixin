from test_selenium.test_projectPO.pages.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    def teardown_class(self):
        self.main.driver.quit()

    def test_add_member(self):
        # 从首页跳转到添加成员页面，添加成员, 点击保存按钮
        namelist = self.main.go_to_add_member().add_member("ez","555","13899991234").save_member().get_member_list()
        assert "ez" in namelist

    def test_add_member_failed(self):
        namelist = self.main.go_to_add_member().add_member("ez2","555","13899991234").cancel_member().get_member_list()
        assert "ez2" not in namelist

    def test_contact_member(self):
        # 从首页跳转到通讯录页面，跳转到添加成员页面，添加成员, 点击保存按钮
        self.main.go_to_contact().go_to_add_member().add_member().save_member()
