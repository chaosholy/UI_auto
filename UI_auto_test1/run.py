
import os
import pytest

# allure_report_path = "--alluredir=test_result/reports"


# 1、生成alluer测试报告数据
pytest.main(["--alluredir=test_result/reports",  # 指定生产allure报告的路径
             '--reruns', '3',  # 指定失败重运行的次数
             '--reruns-delay', '2'  # 指定失败重运行的间隔时间
             ])

# 2、启动allure服务
# os.system('allure serve test_result/reports')


