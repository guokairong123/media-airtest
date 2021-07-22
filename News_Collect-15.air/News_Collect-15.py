# -*- encoding=utf8 -*-
__author__ = "guokairong"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


poco("com.touchtv.leizhou:id/collect").click()

assert_exists(Template(r"tpl1626858227876.png", record_pos=(0.307, 0.832), resolution=(720, 1280)), "新闻内——收藏成功")
sleep(2)

poco("com.touchtv.leizhou:id/collect").click()
assert_exists(Template(r"tpl1626858277114.png", record_pos=(0.307, 0.835), resolution=(720, 1280)), "新闻内——取消收藏")
sleep(2)

poco("com.touchtv.leizhou:id/back").click()

poco.stop_running()