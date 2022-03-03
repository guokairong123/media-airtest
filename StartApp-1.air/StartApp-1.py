# -*- encoding=utf8 -*-
__author__ = "guokairong"

import sys

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
print("参数是:"+str(sys.argv))
name = sys.argv[1]
start_app(sys.argv[1])
sleep(2)
poco(text="测试服务器").click()

sleep(2)
# 隐私弹窗处理
if poco(sys.argv[1]+":id/ckbox").exists():
    poco(sys.argv[1]+":id/ckbox").click()
    poco(sys.argv[1]+":id/push_positive").click()
    poco(sys.argv[1]+":id/tv_ok").click()
    poco("com.android.packageinstaller:id/permission_allow_button").click()
    poco("com.android.packageinstaller:id/permission_allow_button").click()
    sleep(5)
for i in range(3):
    if exists(Template(r"tpl1625825932212.png", record_pos=(-0.017, -0.083), resolution=(1080, 2280))):
        poco("com.touchtv."+sys.argv[1]+":id/negative").click()
        sleep(5)
    else:
        break
try:
    assert_not_exists(Template(r"tpl1625825932212.png", record_pos=(-0.017, -0.083), resolution=(1080, 2280)), "网络正常")
except:
    pass

# 广告跳过
poco(sys.argv[1]+":id/circleProgressbar").click()
try:
    assert_exists(Template(r"tpl1625473069594.png", record_pos=(0.011, -0.76), resolution=(720, 1280)), "进入首页")
except:
    pass
poco.stop_running()



