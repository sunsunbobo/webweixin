from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""

    def __init__(self, driver_base=None):
        # 避免driver重复实例化
        if driver_base is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver = driver_base
        if self._base_url != "":
            self.driver.get(self._base_url)
        self.driver.implicitly_wait(3)

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def wait_for_clickable(self,element):
        # 显式等待元素可被点击
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(element))

    def finds(self, by, value):
        return self.driver.find_elements(by, value)
