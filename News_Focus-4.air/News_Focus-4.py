# -*- encoding=utf8 -*-
__author__ = "guokairong"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 焦点图
sleep(2)
poco("com.touchtv.leizhou:id/img").click()
sleep(3)
poco("com.touchtv.leizhou:id/back").click()
sleep(2)
poco.stop_running()

