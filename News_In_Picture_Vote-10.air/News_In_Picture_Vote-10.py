# -*- encoding=utf8 -*-
__author__ = "guokairong"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
width, height = device().get_current_resolution()
start_pt = (width*0.5, height*0.9)
end_pt = (width*0.5, height*0.1)

swipe(start_pt, end_pt)
poco(text="首页").click()
sleep(2)
swipe(start_pt, end_pt)
poco(text="图片与投票").click()
sleep(2)
assert_exists(Template(r"tpl1626421304787.png", record_pos=(0.004, -0.042), resolution=(720, 1280)), "新闻内——图片显示正常")


swipe(start_pt, end_pt)
if exists(Template(r"tpl1626422941653.png", threshold=0.9, record_pos=(0.013, 0.044), resolution=(720, 1280))):
    print("今天已投票")
else:

    poco("1、一般").click()
    poco("投票").click()
    assert_exists(Template(r"tpl1626422402795.png", record_pos=(0.028, 0.056), resolution=(720, 1280)), "投票成功")

sleep(2)
touch(Template(r"tpl1626423045481.png", record_pos=(-0.003, 0.386), resolution=(720, 1280)))
assert_exists(Template(r"tpl1626423064084.png", record_pos=(0.01, 0.386), resolution=(720, 1280)), "新闻内——点赞成功")
poco.stop_running()



