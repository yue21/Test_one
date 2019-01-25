from appium import webdriver


def get_driver(package, activity):
    # 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps["platformName"] = "Android"
    desired_caps["platformVersion"] = "5.1"
    desired_caps["deviceName"] = "huawei"
    # app信息
    desired_caps["appPackage"] = package
    desired_caps["appActivity"] = activity
    # 中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明驱动对象
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
