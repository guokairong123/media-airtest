# -*- encoding=utf8 -*-
__author__ = "guokairong"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 电视tab
poco(text="电视").click()
sleep(2)
touch(Template(r"tpl1626167427355.png", record_pos=(-0.236, -0.036), resolution=(720, 1280)))

try:
    assert_exists(Template(r"tpl1615185146619.png", record_pos=(-0.249, 0.229), resolution=(720, 1280)), "观看电视")
except:
    pass
sleep(2)
poco("com.touchtv.leizhou:id/back").click()
poco.stop_running()
