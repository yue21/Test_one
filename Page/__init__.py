from selenium.webdriver.common.by import By

# 短信页面元素
'''新建按钮'''
add_but_id = (By.ID, 'com.android.mms:id/action_compose_new')
'''输入手机号码'''
send_phone_id = (By.ID, 'com.android.mms:id/recipients_editor')
'''输入内容'''
send_con_id = (By.ID, 'com.android.mms:id/embedded_text_editor')
'''发送按钮'''
send_id = (By.ID, 'com.android.mms:id/send_button_sms')
'''结果列表'''
res_ids = (By.ID, 'com.android.mms:id/text_view')


