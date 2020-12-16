from test_selenium.test_projectPO.pages.add_member import AddMemberPage
from test_selenium.test_projectPO.pages.basepage import BasePage


class ContactPage(BasePage):
    def go_to_add_member(self):
        return AddMemberPage()

    def get_member_list(self):
        ele = self.find()
        print(ele)
        return [name.text for name in ele]
