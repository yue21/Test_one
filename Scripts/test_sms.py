import sys, os, pytest

sys.path.append(os.getcwd())
from Base.Page_entry_class import Page_obj
from Base.initdriver import get_driver


class Test_sms():
    def setup_class(self):
        # 初始化driver
        self.driver = get_driver('com.android.mms', '.ui.ConversationList')
        # 实例化统一入口类
        self.page_entry_class_obj = Page_obj(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def click_create_and_send_phone(self):
        '''点击新建按钮并输入手机号码'''
        self.page_entry_class_obj.page_sms_obj().click_add_sms_but()
        self.page_entry_class_obj.page_new_sms_obj().send_phone_but('15824898302')

    @pytest.mark.parametrize('data', ['123', '你好', 'hello'])
    def test_send_con_and_click_send_but(self, data):
        '''输入短信内容并点击发送'''
        self.page_entry_class_obj.page_new_sms_obj().input_con_and_send_but(data)
        '''断言'''
        assert data in self.page_entry_class_obj.page_new_sms_obj().get_resulit()
