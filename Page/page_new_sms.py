import Page
from Base.base import Base


class Page_new_sms(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def send_phone_but(self,number):
        '''输入手机号码'''
        self.send_element(Page.send_phone_id,number)

    def input_con_and_send_but(self,text1):
        '''输入短信内容并点击发送'''
        self.send_element(Page.send_con_id,text1)
        self.click_element(Page.send_id)

    def get_resulit(self):
        '''结果列表'''
        result = self.search_elements(Page.res_ids)
        return [ i.text for i in result]
