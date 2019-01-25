import Page
from Base.base import Base


class Page_sms(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_add_sms_but(self):
        '''点击新建短信按钮'''
        self.click_element(Page.add_but_id)
