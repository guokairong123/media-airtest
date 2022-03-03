# -*- encoding=utf8 -*-
__author__ = "guokairong"

from airtest.core.api import *

import sys
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# 一直滑动直到元素出现
width, height = device().get_current_resolution()
start_pt = (width*0.5, height*0.9)
end_pt = (width*0.5, height*0.1)


def search(element):
    for i in range(10):
        if poco(element).exists():
            return poco(element)
        else:
            swipe(start_pt, end_pt)
            sleep(1)


# 新闻
sleep(3)
poco(text="多种类型文章").click()
search("f829f1e5f2c7ab2bad99403eb18ab898").click()
sleep(2)
try:
    assert_exists(Template(r"tpl1625473999706.png", record_pos=(-0.324, -0.182), resolution=(720, 1280)), "图片链接-新闻")
except:
    pass

keyevent("KEYCODE_BACK")
# 直播
search("732643").click()
sleep(5)
try:
    assert_exists(Template(r"tpl1615171912635.png", record_pos=(0.049, -0.26), resolution=(720, 1280)), "图片链接-直播")
except:
    pass

# if poco(sys.argv[1]+":id/ibBack").exists():
#     poco(sys.argv[1]+":id/ibBack").click()
# else:
#     sleep(2)
#     poco(sys.argv[1]+":id/backgroud_img").click()
#     poco(sys.argv[1]+":id/ibBack").click()
keyevent("KEYCODE_BACK")

# 跳转百度
search("www.baidu").click()
sleep(2)
try:
    assert_exists(Template(r"tpl1625624366387.png", record_pos=(-0.015, -0.542), resolution=(720, 1280)), "图片链接-外链")
except:
    pass

keyevent("KEYCODE_BACK")

# 文章内视频播放
end_pt1 = (width*0.5, height*0.4)
for i in range(10):
    if exists(Template(r"tpl1625561658988.png", threshold=0.9, record_pos=(-0.003, -0.35), resolution=(720, 1280))):

        touch(Template(r"tpl1625561658988.png", threshold=0.9, record_pos=(-0.003, -0.35), resolution=(720, 1280)))
        break
    else:
        swipe(start_pt, end_pt1)
sleep(16)
try:
    assert_exists(Template(r"tpl1625561723828.png", record_pos=(-0.003, -0.35), resolution=(720, 1280)), "文章内视频播放")
except:
    pass
# 播放音频
for i in range(10):
    if exists(Template(r"tpl1625553362237.png", threshold=0.9, record_pos=(-0.353, -0.151), resolution=(720, 1280))):

        touch(Template(r"tpl1625553362237.png", threshold=0.9, record_pos=(-0.353, -0.151), resolution=(720, 1280)))
        break
    else:
        swipe(start_pt, end_pt1)

sleep(40)
try:
    assert_exists(Template(r"tpl1625561792905.png", record_pos=(0.074, 0.097), resolution=(720, 1280)), "文章内音频播放")
except:
    pass

# 文字链接
search("新闻").click()
sleep(2)
try:
    assert_exists(Template(r"tpl1625474398855.png", record_pos=(0.008, 0.003), resolution=(720, 1280)), "文字链接-图文")
except:
    pass
keyevent("KEYCODE_BACK")
search("直播").click()
sleep(2)
try:
    assert_exists(Template(r"tpl1615172446749.png", record_pos=(0.022, -0.244), resolution=(720, 1280)), "文字链接-直播")
except:
    pass
keyevent("KEYCODE_BACK")

search("百度").click()
sleep(2)
try:
    assert_exists(Template(r"tpl1625624366387.png", record_pos=(-0.015, -0.542), resolution=(720, 1280)), "文字链接-外链")
except:
    pass
keyevent("KEYCODE_BACK")
poco.stop_running()
