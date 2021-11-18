# -*- encoding=utf8 -*-
__author__ = "guokairong"

import sys

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 电视tab
poco(text="视听").click()
poco(text="电视").click()
sleep(2)
touch(Template(r"tpl1637216348659.png", record_pos=(-0.226, -0.026), resolution=(720, 1280)))

try:
    assert_exists(Template(r"tpl1615185146619.png", record_pos=(-0.249, 0.229), resolution=(720, 1280)), "观看电视")
except:
    pass
sleep(2)
keyevent("KEYCODE_BACK")
poco.stop_running()
