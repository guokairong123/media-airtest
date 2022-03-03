# -*- encoding=utf8 -*-
__author__ = "guokairong"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco(text="服务").click()
sleep(2)
poco(text="服务").click()
assert_exists(Template(r"tpl1637590658017.png", record_pos=(-0.451, -0.658), resolution=(720, 1280)), "正常打开服务tab")

sleep(2)

poco("外链").click()
assert_exists(Template(r"tpl1626860787719.png", record_pos=(0.007, -0.517), resolution=(720, 1280)), "打开服务tab内容")
sleep(2)
keyevent("KEYCODE_BACK")
stop_app(sys.argv[1])
poco.stop_running()