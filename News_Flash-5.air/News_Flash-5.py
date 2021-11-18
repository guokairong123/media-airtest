# -*- encoding=utf8 -*-
__author__ = "guokairong"

import sys

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco(sys.argv[1]+":id/newsFlash_title").click()
sleep(2)
keyevent("KEYCODE_BACK")
poco.stop_running()