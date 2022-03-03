# -*- encoding=utf8 -*-
__author__ = "guokairong"

import sys

from airtest.core.api import *
from airtest.cli.parser import cli_setup

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 一直滑动直到元素出现
width, height = device().get_current_resolution()
start_pt = (width * 0.5, height * 0.9)
end_pt = (width * 0.5, height * 0.1)
swipe(start_pt, end_pt)
poco(text="民声热线0629").click()
sleep(2)
assert_exists(Template(r"tpl1637741083900.png", record_pos=(0.006, 0.278), resolution=(720, 1280)), "图文直播")


# 播放器收起
poco(sys.argv[1] + ":id/iv_expand").click()
sleep(3)
assert_exists(Template(r"tpl1637741101969.png", record_pos=(0.006, -0.715), resolution=(720, 1280)), "播放器收起")


# 播放器展开
poco(sys.argv[1] + ":id/iv_expand").click()
assert_exists(Template(r"tpl1625475633677.png", record_pos=(0.438, -0.261), resolution=(720, 1280)), "播放器展开")

sleep(3)

# 点赞
if poco(text="聊天室").exists():
    poco(text="聊天室").click()
else:
    poco(text="互动").click()
sleep(2)
touch((360, 900), times=20, duration=0.2)

# 媒体号主页订阅功能
poco(sys.argv[1] + ":id/avatar").click()
sleep(1)

# 判断是否已经订阅
if poco(sys.argv[1] + ":id/tv_dingyue").exists():
    poco(sys.argv[1] + ":id/tv_dingyue").click()
else:
    poco(sys.argv[1] + ":id/rl_more").click()
    sleep(2)
    poco(text="取消订阅").click()
    sleep(2)
    poco(sys.argv[1] + ":id/rl_more").click()
    sleep(2)
    poco(text="关闭提醒").click()
    sleep(2)
    poco(sys.argv[1] + ":id/tv_dingyue").click()
sleep(1)
if poco(sys.argv[1] + ":id/tv_remind").exists():
    poco(sys.argv[1] + ":id/tv_remind").click()
sleep(1)
poco(sys.argv[1] + ":id/rl_more").click()
try:
    assert_exists(Template(r"tpl1637223116935.png", record_pos=(-0.328, 0.735), resolution=(720, 1280)), "开播提醒")

except:
    pass
touch((400, 500))
keyevent("KEYCODE_BACK")
sleep(3)
keyevent("KEYCODE_BACK")
poco.stop_running()

