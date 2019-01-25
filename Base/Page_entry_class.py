from Page.page_sms import Page_sms
from Page.page_new_sms import Page_new_sms


class Page_obj:
    def __init__(self, driver):
        self.driver = driver

    def page_sms_obj(self):
        '''返回首页对象'''
        return Page_sms(self.driver)

    def page_new_sms_obj(self):
        '''返回新信息页面对象'''
        return Page_new_sms(self.driver)
