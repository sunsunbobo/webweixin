import shelve

from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options


class TestDemo0():
    def setup(self):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_demo0(self):
        self.driver.get("https://ceshiren.com")
        self.driver.find_element_by_xpath('//a[text()="所有分类"]').click()
        ca = self.driver.find_element_by_xpath('//a[text()="所有分类"]')

        assert 'active' == ca.get_attribute("class")

    def test_cookie(self):
        self.driver.get("")
        cookies = self.driver.get_cookies()
        cookies = [cookie: RK=0By5whumGy; ptcz=006163a64f6efa8cb16b957c01605d6b52223a4399ba7d8aacd554f0fd010ef9; pgv_pvid=1041006029; pac_uid=0_3da00ff7a0122; wwrtx.i18n_lan=zh; wwrtx.c_gdpr=0; _ga=GA1.2.1674864281.1606807754; pgv_info=ssid=s3807849936; _qpsvr_localtk=0.873805032246892; ww_rtkey=5ohioka; wwrtx.ref=direct; wwrtx.refid=8186870913427437; Hm_lvt_9364e629af24cb52acc78b43e8c9f77d=1606807753,1607500644; _gid=GA1.2.953027664.1607500644; _gat=1; Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d=1607500652; wwrtx.d2st=a708907; wwrtx.sid=5SlIhF-e2p6wt43wlWCF5DcZTUZh4O2YUCKLOR9orD7y4xQvHYePxtUsYl7u6O1r; wwrtx.ltype=1; wxpay.corpid=1970324976203057; wxpay.vid=1688853339195185; wwrtx.vst=N3XPbq5uCoKPDQO2ow5rLuNrVJVdhu4KVSZMdVIOUJyShArZQtjh-7fz1wCTUjvljmURAuNkcvIDncvlK-XMKpv_nJGgFcZamuB1a9yeUrdIHEoCel0jKIBciR70aTpu3gMYNmYmNWDXRBvsUTN3cW9OBxxNYjCb_uahl-QFL1dj7BlRgDvW0_FEZHjDVFv_C6hkXNnXjvjY3GCgvflaes7mSpm2Z4izUe_rAYF6HU8cTYSF2Fkys3JKiOckAGY6lCxwxCFSlx3Qhnllp9uIqg; wwrtx.vid=1688853339195185]
        print(cookies)
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("")
        self.driver.find_element_by_xpath('//span[@class="index_service_cnt_item_title"]').click()
        self.driver.find_element_by_xpath('//span[@class="index_service_cnt_item_title"]').send_keys("")

        db = shelve.open('./mydbs/cookies')
        db['cookie'] = cookies
        db.close()
