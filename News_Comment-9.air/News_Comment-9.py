# -*- encoding=utf8 -*-
__author__ = "guokairong"

import sys

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 评论
poco(sys.argv[1]+":id/iv_comment").click()
sleep(2)
if poco("android.widget.TextView").exists():
    poco("android.widget.TextView").click()
else:
    pass
poco(sys.argv[1]+":id/btnEdit").click()
text("测试")
poco(sys.argv[1]+":id/btn_send_comment").click()
try:
    assert_exists(Template(r"tpl1615173133956.png", record_pos=(-0.317, 0.046), resolution=(720, 1280)), "文章评论")
except:
    pass

# 回到首页
keyevent("KEYCODE_BACK")
sleep(2)
keyevent("KEYCODE_BACK")
poco.stop_running()