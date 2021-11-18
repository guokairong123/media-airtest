# -*- encoding=utf8 -*-
__author__ = "guokairong"

import sys

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# 搜索
poco(sys.argv[1]+":id/top_search").click()
poco(sys.argv[1]+":id/search_et").click()
text("测试")
keyevent("Enter")
poco(text="直播").click()
poco(text="媒体").click()
poco(sys.argv[1]+":id/tv_cancel").click()
poco.stop_running()




