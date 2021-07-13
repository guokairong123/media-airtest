# -*- encoding=utf8 -*-
__author__ = "guokairong"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 评论
poco("com.touchtv.leizhou:id/iv_comment").click()
sleep(2)
if poco("android.widget.TextView").exists():
    poco("android.widget.TextView").click()
else:
    pass
poco("com.touchtv.leizhou:id/btnEdit").click()
text("测试")
poco("com.touchtv.leizhou:id/btn_send_comment").click()
try:
    assert_exists(Template(r"tpl1615173133956.png", record_pos=(-0.317, 0.046), resolution=(720, 1280)), "文章评论")
except:
    pass

# 回到首页
poco("com.touchtv.leizhou:id/ivGoBack").click()
poco("com.touchtv.leizhou:id/back").click()
poco.stop_running()