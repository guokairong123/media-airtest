# -*- encoding=utf8 -*-
__author__ = "guokairong"

import sys

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def logout():
    poco(sys.argv[1]+":id/img_setting").click()
    poco(sys.argv[1]+":id/scrollView").swipe([-0.0253, -0.1157])
    poco(sys.argv[1]+":id/tv_loginout").click()
    poco(sys.argv[1]+":id/positive").click()


poco(sys.argv[1]+":id/top_userHead").click()
if poco(sys.argv[1]+":id/userName_nologin").exists():
    pass
else:
    logout()

# # 微博登录
#
# poco(sys.argv[1]+":id/userName_nologin").click()
# poco(sys.argv[1]+":id/checkbox").click()
# poco(sys.argv[1]+":id/iv_weibo").click()
# sleep(5)
# poco("com.sina.weibo:id/new_bnLogin").click()
# sleep(2)
# if poco(text="完善个人信息，让大家更懂你").exists():
#     poco(text="完善个人信息，让大家更懂你").click()
# try:
#     assert_not_exists(Template(r"tpl1626163001924.png", record_pos=(0.017, -0.188), resolution=(720, 1280)), "微博登录")
#     logout()
# except:
#     print("微博登录失败")
#
# # QQ登录
# if poco(sys.argv[1]+":id/userName_nologin").exists():
#     poco(sys.argv[1]+":id/userName_nologin").click()
# else:
#     poco(sys.argv[1]+":id/checkbox").click()
# poco(sys.argv[1]+":id/checkbox").click()
# poco(sys.argv[1]+":id/iv_qq").click()
# sleep(5)
# poco("com.tencent.mobileqq:id/fds").click()
# sleep(2)
# try:
#     assert_not_exists(Template(r"tpl1626163001924.png", record_pos=(0.017, -0.188), resolution=(720, 1280)), "QQ登录")
#     logout()
# except:
#     print("QQ登录失败")
#
# # 微信登录
# if poco(sys.argv[1]+":id/userName_nologin").exists():
#     poco(sys.argv[1]+":id/userName_nologin").click()
# else:
#     poco(sys.argv[1]+":id/iv_weixin").click()
# poco(sys.argv[1]+":id/checkbox").click()
# poco(sys.argv[1]+":id/iv_weixin").click()
# sleep(5)
# # 没有微信账号
# if poco("com.tencent.mm:id/d5n").exists():
#     poco("com.tencent.mm:id/dn").click()
#
# sleep(2)
# try:
#     assert_not_exists(Template(r"tpl1626163001924.png", record_pos=(0.017, -0.188), resolution=(720, 1280)), "微信登录")
#     logout()
# except:
#     print("没有微信账号")

sleep(2)
# 手机号登录
if poco(sys.argv[1]+":id/userName_nologin").exists():
    poco(sys.argv[1]+":id/userName_nologin").click()
else:
    poco(sys.argv[1]+":id/checkbox").click()
poco(sys.argv[1]+":id/mobileNumber").set_text("17876253458")
poco(sys.argv[1]+":id/password").set_text("q992926186")
poco(sys.argv[1]+":id/checkbox").click()
poco(sys.argv[1]+":id/btn_login").click()
sleep(2)
try:
    assert_exists(Template(r"tpl1625646326839.png", record_pos=(-0.001, -0.637), resolution=(720, 1280)), "手机号登录")
except:
    print("手机号登录失败")
if poco(text="完善个人信息，让大家更懂你").exists():
    poco(text="完善个人信息，让大家更懂你").click()
poco(sys.argv[1]+":id/ll_goback").click()
poco.stop_running()


