# -*- encoding=utf8 -*-
__author__ = "guokairong"

import sys

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco(text="视频").click()
sleep(2)
poco(sys.argv[1]+":id/startPlay")[0].click()
sleep(31)
assert_exists(Template(r"tpl1637291414067.png", record_pos=(0.004, -0.368), resolution=(720, 1280)), "视频tab-播放视频")


poco(sys.argv[1]+":id/like_btn").click()
sleep(2)
assert_exists(Template(r"tpl1626419943840.png", record_pos=(0.344, 0.019), resolution=(720, 1280)), "视频tab-点赞")

poco(sys.argv[1]+":id/publisher").click()
sleep(2)
assert_exists(Template(r"tpl1637217514335.png", record_pos=(0.01, 0.8), resolution=(720, 1280)), "视频tab-跳转到视频详情页")

keyevent("KEYCODE_BACK")

poco.stop_running()
