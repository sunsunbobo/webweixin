from selenium import webdriver
from selenium.webdriver.common.by import By

from test_selenium.test_projectPO.pages.basepage import BasePage
from test_selenium.test_projectPO.pages.contact_page import ContactPage


class AddMemberPage(BasePage):
    _username = (By.ID, "username")
    _acctid = (By.ID, "memberAdd_acctid")
    _memberAdd_phone = (By.ID, "memberAdd_phone")
    _cancel = (By.ID, "cancel")

    def add_member(self, name, acctid, memberAdd_phone):
        self.find(*self._username).send_keys(name)
        self.find(*self._acctid).send_keys(acctid)
        self.find(*self._memberAdd_phone).send_keys(memberAdd_phone)
        # 返回self是为了实现返回当前页面时依然可以实现链式调用  相当于，别人调用时，add_member(),save_member(),就等同于self.save_member(self)
        return self

    def save_member(self):
        # 点击保存按钮
        self.find().click()
        return ContactPage(self.driver)

    def cancel_member(self):
        self.find().click()
        self.wait_for_clickable(self._cancel)
        return ContactPage(self.driver)
