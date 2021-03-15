from selenium.webdriver.common.by import By

from common.base_page import BasePage


class EduManagePage(BasePage):
    """教务管理"""
    url = ''
    submenu_classes_manage = (By.XPATH, '//div//span[@class="ds-aside-menu-item-name" and text()="班次管理"]')  # 班次管理
    submenu_teaching_manage = (By.XPATH, '//span[text()="教学管理"]/parent::div')  # 教学管理
    week_Timetable = (
        By.XPATH, '//font[text()="一周课表"]/ancestor::div[@class="ds-aside-menu-item-box"]')  # 一周课表
    teach_plan = (By.XPATH, '//font[text()="教学计划"]/ancestor::div[@class="ds-aside-menu-item-box"]')  # 教学计划
    class_arrangement = (
        By.XPATH, '//font[text()="排课管理"]/ancestor::div[@class="ds-aside-menu-item-box"]')  # 排课管理
    transferring_classes = (
        By.XPATH, '//font[text()="调课记录"]/ancestor::div[@class="ds-aside-menu-item-box"]')  # 调课记录
    submenu_task_manage = (By.XPATH, '//span[text()="作业管理"]/parent::div[@style="padding-left: 20px;"]')  # 作业管理
    task_manage = (By.XPATH, '//font[text()="作业管理"]/ancestor::li[@class="ds-aside-menu-item"]/div')  # 作业管理
    task_Review = (By.XPATH, '//font[text()="作业批阅"]/ancestor::div[@class="ds-aside-menu-item-box"]')  # 作业批阅
    results_registration = (By.XPATH, '//font[text()="成绩登记"]/ancestor::div[@class="ds-aside-menu-item-box"]')  # 成绩登记
    submenu_notice_manage = (By.XPATH, '//span[text()="通知公告"]/parent::div')  # 通知公告
    submenu_teaching_evaluation_manage = (By.XPATH, '//span[text()="教学评价管理"]/parent::div')  # 教学评价管理
    submenu_teaching_data = (By.XPATH, '//span[text()="教学资料"]/parent::div')  # 教学资料
    submenu_certificate_print = (By.XPATH, '//span[text()="证书打印"]/parent::div')  # 证书打印
    submenu_my_schedule = (By.XPATH, '//span[text()="我的课表"]/parent::div')  # 我的课表
    submenu_student_info = (By.XPATH, '//span[text()="学员信息查询"]/parent::div')  # 学员信息查询
    submenu_teaching_set = (By.XPATH, '//span[text()="教学设置"]/parent::div')  # 教学设置
