import allure
from Base.base import Base
import Page


class PageAddress(Base):
    # 封装设置
    @allure.step("点击设置")
    def page_address_btn_image(self):
        self.base_click(Page.address_btn_image)
    # 封装 地址管理
    @allure.step("点击地址管理")
    def page_address_manage(self):
        self.base_click(Page.address_manage)
    # 新增地址
    @allure.step("点击新增地址")
    def page_address_add_new(self):
        self.base_click(Page.address_add_new)
    # 收件人
    @allure.step("收件人")
    def page_address_receipt_name(self,receipt_name):
        self.base_input(Page.address_receipt_name,receipt_name)
    # 手机号
    @allure.step("手机号")
    def page_address_add_phone(self, add_phone):
        self.base_input(Page.address_add_phone, add_phone)
    # 所在区域
    @allure.step("所在区域")
    def page_address_province(self,sheng,shi,qu):
        self.base_click(Page.address_province)
        self.base_xpath(sheng).click()
        self.base_xpath(shi).click()
        self.base_xpath(qu).click()
    # 详细地址
    @allure.step("详细地址")
    def page_address_detail_addr(self, detail_addr):
        self.base_input(Page.address_detail_addr, detail_addr)
    # 邮编
    # @allure.step("邮编")
    def page_address_post_code(self, post_code):
        self.base_input(Page.address_post_code, post_code)
    # 设置默认地址
    @allure.step("设置默认地址")
    def page_address_default(self):
        self.base_click(Page.address_default)
    # 保存
    @allure.step("保存")
    def page_address_button_send(self):
        self.base_click(Page.address_button_send)
    # 获取收件人和电话
    def page_get_recipit_and_phone(self):
        self.base_input(Page.address_receipt_and_phone)
    # 编辑
    @allure.step("编辑")
    def page_address_right_btn(self):
        self.base_click(Page.address_right_btn)
    # 修改
    def page_address_modify(self):
        self.base_click(Page.address_modify)
    # 点击删除
    def page_address_delete(self):
        self.base_click(Page.address_delete)
    # 确认删除
    def page_address_delete_ok(self):
        self.base_click(Page.address_delete_ok)

    def page_is_delete(self):
        try:
            self.base_find_element(Page.address_receipt_and_phone, timeout=3)
            return False
        except:
            return True