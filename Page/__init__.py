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