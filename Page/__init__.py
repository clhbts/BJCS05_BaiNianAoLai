from selenium.webdriver.common.by import By
"""
    以下为：百年奥莱APP登录数据
"""
# 点击我
me_btn="我"
# 点击已有账户，去登录
user="已有账号"
# 输入用户名
user_name=By.ID,"com.yunmall.lc:id/logon_account_textview"
# 输入密码
user_pwd=By.ID,"com.yunmall.lc:id/logon_password_textview"
# 点击登录按钮
login_btn=By.ID,"com.yunmall.lc:id/logon_button"
# 点击设置按钮
setting_btn=By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
"""消息推送  -->  滑到--->修改密码"""
# 消息推送
msg_send="消息推送"
# 修改密码
update_pwd="修改密码"
# 点击退出按钮
exit_btn="退出"
# 点击确认按钮
exit_ok="确认"
# 获取昵称
me_nickname=By.ID,"com.yunmall.lc:id/tv_user_nikename"
"""
地址管理的增加   
"""
# 设置
address_btn_image=By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 地址管理
address_manage=By.ID,"com.yunmall.lc:id/setting_address_manage"
# 新增地址
address_add_new=By.ID,"com.yunmall.lc:id/address_add_new_btn"
# 收件人
address_receipt_name=By.ID,"com.yunmall.lc:id/address_receipt_name"
# 手机号
address_add_phone=By.ID,"com.yunmall.lc:id/address_add_phone"
# 所在区域
address_province=By.ID,"com.yunmall.lc:id/address_province"
# 详细地址
address_detail_addr=By.ID,"com.yunmall.lc:id/address_detail_addr_info"
# 邮编
address_post_code=By.ID,"com.yunmall.lc:id/address_post_code"
# 设置默认地址
address_default=By.ID,"com.yunmall.lc:id/address_default"
# 保存
address_button_send=By.ID,"com.yunmall.lc:id/button_send"
# 收件人+电话
address_receipt_and_phone=By.ID,"com.yunmall.lc:id/receipt_name"
"""修改"""
# 编辑
address_right_btn=By.ID,"com.yunmall.lc:id/ymtitlebar_right_btn"
# 修改
address_modify=By.ID,"com.yunmall.lc:id/modify"
# 删除
address_delete=By.ID,"com.yunmall.lc:id/delete"
# 确认删除
address_delete_ok=By.ID,"com.yunmall.lc:id/ymdialog_left_button"
