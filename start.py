import io
import os
import shutil
from argparse import *
import jinja2
from airtest.cli.runner import AirtestCase
from airtest.cli.runner import run_script
from airtest.core.android import adb
from airtest.core.api import sleep
from airtest.core.helper import *

from airtest.report import report
from logger import logger


class Start(AirtestCase):
    def setUp(self):
        print("test setup")
        super(Start, self).setUp()

    def tearDown(self):
        print("test teardown")
        super(Start, self).tearDown()

    def run(self, root_dir="/Users/guokairong/Downloads/media-airtest", device=['Android://127.0.0.1:5037/emulator-5554']):
        # 聚合报告存储
        results = []
        args = []
        listdirs = []
        # 日志存储路径
        root_log = root_dir + '/' + 'log'

        # 查询日志路径是否已经存在，有则删除里面的内容，否则创建该路径
        if os.path.isdir(root_log):
            shutil.rmtree(root_log)
        else:
            os.makedirs(root_log)
            print(str(root_log) + ' is created')
        # 验证文件夹后缀是否为".air"，并生产路径
        for listdir in os.listdir(root_dir):
            if listdir.endswith('.air'):
                listdirs.append(listdir)
        # 对文件自定义排序
        listdirs.sort(key=lambda x: int(x.split('-')[1].split('.air')[0]))
        for f in listdirs:
            airName = f
            script = os.path.join(root_dir, f)
            print(script)
            # 每个用例日志的存储路径
            log = os.path.join(root_dir, 'log' + '/' + airName.replace('.air', ''))
            print(log)
            if os.path.isdir(log):
                shutil.rmtree(log)
            else:
                os.makedirs(log)
                print(str(log) + ' is created')
            # 命令行参数，解析获得后的数据格式Namespace(device=device, log=log, recording=None, script=script)
            # python -m airtest-media run /Users/guokairong/Downloads/airtest-media/news1.air  --device Android://127.0.0.1:5037/emulator-5554  --log "/Users/guokairong/Downloads/airtest-media/log/news1"
            args = Namespace(device=device, compress=10, no_image=None, log=log, recording=None, script=script)
            try:
                sleep(3)
                run_script(args, AirtestCase)
            except:
                pass
            finally:
                # 日志输出文件
                output_file = log + '/' + 'log.html'
                rpt = report.LogToHtml(script, log)
                rpt.report("log_template.html", output_file=output_file)
                # simple_report(script, logpath=log, output=output_file)
                logger.info("执行完成")
                result = {"name": airName.replace('.air', ''), "result": rpt.test_result}
                results.append(result)
                G.DEVICE.adb.kill_server()
                # os.system("killall -e adb")
                # sleep(5)
        # 生成聚合报告
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(root_dir),
            extensions=(),
            autoescape=True
        )
        template = env.get_template("report_template.html", root_dir)
        html = template.render({"results": results})
        print("结果:", results)
        output_file = os.path.join(root_dir, "report.html")
        with io.open(output_file, 'w', encoding="utf-8") as f:
            f.write(html)


if __name__ == '__main__':
    test = Start()
    # 连接的设备
    device = ['Android://127.0.0.1:5037/emulator-5554']
    # 项目根目录
    test.run('/Users/guokairong/Downloads/media-airtest', device)
