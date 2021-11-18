# -*- encoding=utf8 -*-
__author__ = "guokairong"

import sys

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 焦点图
sleep(2)
poco(sys.argv[1]+":id/img").click()
sleep(3)
keyevent("KEYCODE_BACK")
sleep(2)
poco.stop_running()

