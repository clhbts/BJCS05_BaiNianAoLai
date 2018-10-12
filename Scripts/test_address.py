import os, sys
sys.path.append(os.getcwd())

import pytest
from Base.read_address_yaml import ReadAddressYaml
import allure
from Page.page_in import PageIn
from Base.get_driver import get_driver


def get_data(text_type):
    datas = ReadAddressYaml("address.yaml").read_address_yaml02()
    arrs = []
    if text_type=="add":
        for data in datas.get("add_address").values():
            arrs.append((
                        data.get("receipt_name"), data.get("add_phone"), data.get("sheng"), data.get("shi"), data.get("qu"),
                        data.get("detail_addr"), data.get("post_code")))
        return arrs
    elif text_type=="update":
        for data in datas.get("update_address").values():
            arrs.append((
                data.get("receipt_name"), data.get("add_phone"), data.get("sheng"), data.get("shi"), data.get("qu"),
                data.get("detail_addr"), data.get("post_code")))
        return arrs


class TestAddress():
    def setup_class(self):
        # 实例化 登录页面类
        self.page = PageIn(get_driver())
        self.page.page_get_login().page_login("zhangsan", "123456")
        # 实例化 PageAddress
        self.address = self.page.page_get_address()
        # 点击设置
        self.address.page_address_btn_image()
        # 点击地址管理
        self.address.page_address_manage()

    def teardown_class(self):
        # 退出driver驱动
        self.address.driver.quit()

    # 地址管理 数据添加
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("receipt_name,add_phone,sheng,shi,qu,detail_addr,post_code", get_data("add"))
    def test_add_address(self, receipt_name, add_phone, sheng, shi, qu, detail_addr, post_code):
        # 点击新增
        self.address.page_address_add_new()
        # 输入 收件人
        self.address.page_address_receipt_name(receipt_name)
        #  输入 手机号
        self.address.page_address_add_phone(add_phone)
        # 选择 所在区域
        self.address.page_address_province(sheng, shi, qu)
        #  输入 详细地址
        self.address.page_address_detail_addr(detail_addr)
        # # 输入 邮编
        self.address.page_address_post_code(post_code)
        # 点击 设置默认地址
        self.address.page_address_default()
        # # 点击 保存
        self.address.page_address_button_send()
        try:
            # 断言 是否新增成功
            # print("获取新增地址联系人和电话为：",self.address.page_get_recipit_and_phone())
            assert receipt_name in self.address.page_get_recipit_and_phone()
        except:
            # 截图
            self.login.base_getImage()
            with open("./Image/faild.png", "rb") as f:
                allure.attach("断言失败描述：", f.read(), allure.attach_type.PNG)
            # 抛异常
            raise

    # 地址管理 数据修改
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("receipt_name,add_phone,sheng,shi,qu,detail_addr,post_code", get_data("update"))
    def test_update_address(self, receipt_name, add_phone, sheng, shi, qu, detail_addr, post_code):
        # 点击编辑
        self.address.page_address_right_btn()
        # 点击修改
        self.address.page_address_modify()
        """ 修改内容"""
        # 输入 收件人
        self.address.page_address_receipt_name(receipt_name)
        # 输入 手机号
        self.address.page_address_add_phone(add_phone)
        # 选择 所在区域
        self.address.page_address_province(sheng, shi, qu)
        # 输入 详细地址
        self.address.page_address_detail_addr(detail_addr)
        # 输入 邮编
        self.address.page_address_post_code(post_code)
        # 点击 保存
        self.address.page_address_button_send()
        try:
            # 断言 是否修改成功
            assert receipt_name in self.address.page_get_recipit_and_phone()
        except:
            # 截图
            self.login.base_getImage()
            with open("./Image/faild.png", "rb") as f:
                allure.attach("断言失败描述：", f.read(), allure.attach_type.PNG)
            # 抛异常
            raise

    # 地址管理 数据删除
    @pytest.mark.run(order=3)
    def test_delect_address(self):
        # 点击编辑
        self.address.page_address_right_btn()
        # 点击删除
        self.address.page_address_delete()
        # 确认删除
        self.address.page_address_delete_ok()
        try:
            # 断言 是否修改成功
            assert self.address.page_is_delete()
        except:
            # 截图
            self.login.base_getImage()
            with open("./Image/faild.png", "rb") as f:
                allure.attach("断言失败描述：", f.read(), allure.attach_type.PNG)
            # 抛异常
            raise
