# -*- encoding=utf8 -*-
__author__ = "guokairong"

from airtest.core.api import sleep
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco("com.touchtv.leizhou:id/newsFlash_title").click()
sleep(2)
poco("com.touchtv.leizhou:id/back").click()
poco.stop_running()