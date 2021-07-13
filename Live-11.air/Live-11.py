# -*- encoding=utf8 -*-
__author__ = "guokairong"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


poco(text="直播").click()
sleep(2)
assert_exists(Template(r"tpl1625475476419.png", record_pos=(0.001, -0.76), resolution=(720, 1280)), "切换tab")


sleep(2)
touch(Template(r"tpl1625475510697.png", record_pos=(0.033, -0.468), resolution=(720, 1280)))
assert_exists(Template(r"tpl1625475535929.png", record_pos=(-0.004, -0.557), resolution=(720, 1280)), "直播专题")

sleep(2)
poco("com.touchtv.leizhou:id/back").click()
poco(text="图文直播3").click()
sleep(2)
assert_exists(Template(r"tpl1625475611489.png", record_pos=(0.042, 0.224), resolution=(720, 1280)), "图文直播")


# 播放器收起
poco("com.touchtv.leizhou:id/iv_expand").click()
sleep(3)
assert_exists(Template(r"tpl1625475587496.png", record_pos=(0.0, -0.717), resolution=(720, 1280)), "播放器收起")

# 播放器展开
poco("com.touchtv.leizhou:id/iv_expand").click()
assert_exists(Template(r"tpl1625475633677.png", record_pos=(0.438, -0.261), resolution=(720, 1280)), "播放器展开")

sleep(3)

# 点赞
poco(text="聊天室").click()
sleep(2)
touch((360, 900), times=20, duration=0.2)

# 媒体号主页订阅功能
poco("com.touchtv.leizhou:id/avatar").click()
sleep(1)

# 判断是否已经订阅
if poco("com.touchtv.leizhou:id/tv_dingyue").exists():
    poco("com.touchtv.leizhou:id/tv_dingyue").click()
else:
    poco("com.touchtv.leizhou:id/rl_more").click()
    sleep(2)
    poco(text="取消订阅").click()
    sleep(2)
    poco("com.touchtv.leizhou:id/rl_more").click()
    sleep(2)
    poco(text="关闭提醒").click()
    sleep(2)
    poco("com.touchtv.leizhou:id/tv_dingyue").click()
sleep(1)
poco("com.touchtv.leizhou:id/tv_remind").click()
sleep(1)
poco("com.touchtv.leizhou:id/rl_more").click()
try:
    assert_exists(Template(r"tpl1615184842043.png", record_pos=(-0.338, 0.731), resolution=(720, 1280)), "订阅成功")
except:
    pass
touch((400, 500))
poco("com.touchtv.leizhou:id/rl_back").click()
sleep(3)
poco("com.touchtv.leizhou:id/backgroud_img").click()
if poco("com.touchtv.leizhou:id/ib_back_replay").exists():
    poco("com.touchtv.leizhou:id/ib_back_replay").click()
else:
    poco("com.touchtv.leizhou:id/ibBack").click()
poco.stop_running()
