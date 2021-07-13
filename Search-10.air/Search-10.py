# -*- encoding=utf8 -*-
__author__ = "guokairong"
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# 搜索
poco("com.touchtv.leizhou:id/top_search").click()
poco("com.touchtv.leizhou:id/search_et").click()
text("测试")
keyevent("Enter")
poco(text="直播").click()
poco(text="媒体").click()
poco("com.touchtv.leizhou:id/tv_cancel").click()
poco.stop_running()




