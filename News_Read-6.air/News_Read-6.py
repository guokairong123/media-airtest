# -*- encoding=utf8 -*-
__author__ = "guokairong"

import sys

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

width, height = device().get_current_resolution()
start_pt = (width*0.5, height*0.7)
end_pt = (width*0.5, height*0.2)

# 视频
poco(sys.argv[1]+":id/play_img").click()
poco(sys.argv[1]+":id/imv_like").click()
poco(sys.argv[1]+":id/weMediaAvatarUrl").click()
keyevent("KEYCODE_BACK")
sleep(3)
keyevent("KEYCODE_BACK")
sleep(5)

swipe(start_pt, end_pt)
# 图文
poco(text="纯文字新闻").click()
sleep(2)
try:
    assert_exists(Template(r"tpl1625474343659.png", record_pos=(-0.286, -0.631), resolution=(720, 1280)), "打开纯文字新闻")
except:
    pass
keyevent("KEYCODE_BACK")

# 图集
poco(text="图集新闻啦").click()
try:
    assert_exists(Template(r"tpl1625474398855.png", record_pos=(0.008, 0.003), resolution=(720, 1280)), "打开图集")
except:
    pass
keyevent("KEYCODE_BACK")
poco.stop_running()
