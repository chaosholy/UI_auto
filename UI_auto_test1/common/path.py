# encoding=utf-8

"""
============================
Author:何超
Time:2021/3/2   15:20
============================
"""
import os

# 项目的根目录
base_dir = os.path.dirname(os.path.dirname(__file__))
# # 测试用例数据的目录路径
caseData_dir = os.path.join(base_dir, 'casedata')
# 公共类工具的目录路径
common_dir = os.path.join(base_dir, 'common')
# 配置文件的目录路径
config_dir = os.path.join(base_dir, 'config')
# 页面类的目录路径
page_dir = os.path.join(base_dir, 'page')
# 测试脚本的目录路径
testCase_dir = os.path.join(base_dir, 'testcase')
# 测试报告的目录路径
testReport_dir = os.path.join(base_dir, 'testreport')
#测试结果的目录路径
testResult_dir = os.path.join(base_dir, 'test_result')
#日志的目录路径
log_dir = os.path.join(base_dir,'test_result/logs')
#其他的目录路径
other_dir = os.path.join(base_dir,'others')
