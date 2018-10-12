import os, sys
sys.path.append(os.getcwd())

import allure
import pytest
from Page.page_login import PageLogin
from Base.get_driver import get_driver
from Base.read_yaml import ReadYaml


def get_data():
    datas = ReadYaml("login.yaml").read_yaml()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("username"), data.get("password"), data.get("expect"), data.get("toast_expect")))
    return arrs

class TestLogin():
    def setup_class(self):
        # 实例化 登录页面类
        self.login = PageLogin(get_driver())
        # 点击我
        self.login.page_click_me()
        # 点击已有账户
        self.login.page_click_info()

    def teardown_class(self):
        # 退出driver驱动
        self.login.driver.quit()

    @pytest.mark.parametrize("username,password,expect,toast_expect",get_data())
    def test_login(self, username, password, expect, toast_expect):
        if expect:
            try:
                # 输入用户名
                self.login.page_input_user(username)
                # 输入密码
                self.login.page_input_pwd(password)
                # 点击登录
                self.login.page_click_login_btn()
                # 断言
                assert expect in self.login.page_get_nickname()
                allure.attach("描述:","登录成功")
                # 退出操作
                self.login.page_login_logout()
                # 点击我
                self.login.page_click_me()
                # 点击已有账户
                self.login.page_click_info()
            except:
                # 截图
                self.login.base_getImage()
                with open("./Image/faild.png", "rb") as f:
                    allure.attach("失败描述：", f.read(), allure.attach_type.PNG)
                # 抛异常
                raise

        else:
            try:
                # 输入用户名
                self.login.page_input_user(username)
                # 输入密码
                self.login.page_input_pwd(password)
                # 点击登录
                self.login.page_click_login_btn()
                # 断言
                assert toast_expect in self.login.base_get_toast(toast_expect)
                allure.attach("断言描述","逆向断言成功")
            except:
                # 截图
                self.login.base_getImage()
                with open("./Image/faild.png", "rb") as f:
                    allure.attach("断言失败描述：", f.read(), allure.attach_type.PNG)
                # 抛异常
                raise
