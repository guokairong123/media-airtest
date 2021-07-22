# -*- encoding=utf8 -*-
__author__ = "guokairong"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco(text="视频").click()
sleep(2)
poco("com.touchtv.leizhou:id/startPlay")[0].click()
sleep(31)
assert_exists(Template(r"tpl1626419745600.png", record_pos=(-0.003, -0.408), resolution=(720, 1280)), "视频tab-播放视频")

poco("com.touchtv.leizhou:id/like_btn").click()
sleep(2)
assert_exists(Template(r"tpl1626419943840.png", record_pos=(0.344, 0.019), resolution=(720, 1280)), "视频tab-点赞")


poco(text="雷州G").click()
sleep(2)
assert_exists(Template(r"tpl1626419893540.png", record_pos=(-0.285, 0.067), resolution=(720, 1280)), "视频tab-跳转到视频详情页")
poco("com.touchtv.leizhou:id/back").click()

poco.stop_running()
