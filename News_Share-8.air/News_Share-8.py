# -*- encoding=utf8 -*-
__author__ = "guokairong"

import sys

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def search(element):
    for i in range(10):
        if poco(element).exists():
            return poco(element)
        else:
            swipe(start_pt, end_pt)
            sleep(1)


# 一直滑动直到元素出现
width, height = device().get_current_resolution()
start_pt = (width*0.5, height*0.9)
end_pt = (width*0.5, height*0.1)
end_pt1 = (width*0.5, height*0.4)
i = 0
# QQ分享
for i in range(10):
    if exists(Template(r"tpl1625560879193.png", record_pos=(0.347, 0.7), resolution=(720, 1280))):

        touch(Template(r"tpl1625560879193.png", record_pos=(0.347, 0.7), resolution=(720, 1280)))
        break
    else:
        swipe(start_pt, end_pt1)

poco(text="我的电脑").wait_for_appearance(timeout=20)
poco(text="我的电脑").click()
poco("android.widget.FrameLayout").offspring("com.tencent.mobileqq:id/dialogRightBtn").click()
try:
    assert_exists(Template(r"tpl1615172993000.png", record_pos=(-0.001, 0.021), resolution=(720, 1280)), "QQ分享")
except:
    print("分享失败")

poco("android.widget.FrameLayout").offspring("com.tencent.mobileqq:id/dialogLeftBtn").click()
# 微信分享
search("ico_share_wechat").click()
sleep(2)
if poco("com.tencent.mm:id/d5n").exists():
    assert_exists(Template(r"tpl1626166204584.png", record_pos=(-0.09, -0.607), resolution=(720, 1280)), "微信账号未登录")
    poco("com.tencent.mm:id/dn").click()
else:       
    poco("com.tencent.mm:id/gbv").wait_for_appearance(timeout=20)
    poco("com.tencent.mm:id/gbv").click()
    poco("android.widget.FrameLayout").offspring("android:id/content").offspring("com.tencent.mm:id/doz").click()
    assert_exists(Template(r"tpl1615172661669.png", record_pos=(-0.003, 0.025), resolution=(720, 1280)), "微信分享")
    poco("android.widget.FrameLayout").offspring("android:id/content").offspring("com.tencent.mm:id/dom").click()
   
# 微信朋友圈分享   
poco("ico_share_wechat_circle").click()
sleep(2)
if poco("com.tencent.mm:id/d5n").exists():
    assert_exists(Template(r"tpl1626166204584.png", record_pos=(-0.09, -0.607), resolution=(720, 1280)),"微信账号未登录")
    poco("com.tencent.mm:id/dn").click()
else:
    poco("android.widget.LinearLayout").offspring("android:id/text1").wait_for_appearance(timeout=20)
    sleep(2)
    poco("com.tencent.mm:id/ch").click()
    assert_exists(Template(r"tpl1615172767779.png", record_pos=(0.015, 0.029), resolution=(720, 1280)),  "微信朋友圈分享")

# 微博分享

poco("ico_share_weibo").click()
sleep(5)
if poco(sys.argv[1]+":id/tv_title").exists():
    poco(sys.argv[1]+":id/tv_ok").click()
    poco("com.android.packageinstaller:id/permission_allow_button").click()
else:
    pass
poco("android:id/content").offspring("com.sina.weibo:id/titleSave").wait_for_appearance(timeout=20)
poco("android:id/content").offspring("com.sina.weibo:id/titleSave").click()
poco(text="返回第三方").click()
try:
    assert_exists(Template(r"tpl1615172767779.png", record_pos=(0.015, 0.029), resolution=(720, 1280)), "微博分享")
except:
    print("分享失败")


poco.stop_running()

