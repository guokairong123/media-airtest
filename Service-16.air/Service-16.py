# -*- encoding=utf8 -*-
__author__ = "guokairong"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco(text="服务").click()
sleep(2)

assert_exists(Template(r"tpl1626858546701.png", record_pos=(-0.353, -0.404), resolution=(720, 1280)), "正常打开服务tab")
sleep(2)

poco("外链").click()
assert_exists(Template(r"tpl1626860787719.png", record_pos=(0.007, -0.517), resolution=(720, 1280)), "打开服务tab内容")
sleep(2)
keyevent("KEYCODE_BACK")
poco.stop_running()
