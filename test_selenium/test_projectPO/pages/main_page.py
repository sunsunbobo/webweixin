from selenium import webdriver

from test_selenium.test_projectPO.pages.add_member import AddMemberPage
from test_selenium.test_projectPO.pages.basepage import BasePage
from test_selenium.test_projectPO.pages.contact_page import ContactPage


class MainPage(BasePage):
    _base_url = ""

    def go_to_contact(self):
        self.find().click()
        return ContactPage(self.driver)

    def go_to_add_member(self):
        self.find().click()
        return AddMemberPage(self.driver)
