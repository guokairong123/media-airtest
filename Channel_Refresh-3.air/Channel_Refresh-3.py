# -*- encoding=utf8 -*-
__author__ = "guokairong"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

width, height = device().get_current_resolution()
start_pt = (width*0.5, height*0.4)
end_pt = (width*0.5, height*0.2)
# 刷新操作
swipe(end_pt, start_pt)
sleep(2)

swipe(end_pt, start_pt)

sleep(2)
poco.stop_running()