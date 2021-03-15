# encoding=utf-8

"""
============================
Author:何超
Time:2021/3/2   13::30
============================
"""
from selenium.webdriver.common.by import By
from common.base_page import BasePage


class HomePage(BasePage):
    """主页"""
    url = 'dsf5/index.html'
    user_type = (By.XPATH, '//div[@role="button"]//div[@class="username"]')  # 职务
    menu_headmaster_home = (By.XPATH, '//div[text()="班主任首页"]/parent::div[@class="header-menu-item-box"]')  # 班主任首页
    menu_edu_manage = (By.XPATH, '//div[text()="教务管理"]/parent::div[@class="header-menu-item-box"]')  # 教务管理
    menu_headmaster_manage = (By.XPATH, '//div[text()="班主任管理"]/parent::div[@class="header-menu-item-box"]')  # 班主任管理
    menu_teaching_resources = (By.XPATH, '//div[text()="教学资源"]/parent::div[@class="header-menu-item-box"]')  # 教学资源
    menu_hr_resources = (By.XPATH, '//span[text()="人事管理"]/parent::div')  # 人事管理
    menu_sign_up_manage = (By.XPATH, '//div[text()="报名管理"]/parent::div[@class="header-menu-item-box"]')  # 报名管理
    menu_stay_manage = (By.XPATH, '//div[text()="住宿管理"]/parent::div[@class="header-menu-item-box"]')  # 住宿管理
    menu_question_manage = (By.XPATH, '//div[text()="问卷管理"]/parent::div[@class="header-menu-item-box"]')  # 问卷管理
    menu_sms_platform = (By.XPATH, '//div[text()="短信平台"]/parent::div[@class="header-menu-item-box"]')  # 短信平台
    menu_exam_sys = (By.XPATH, '//div[text()="考试系统"]/parent::div[@class="header-menu-item-box"]')  # 考试系统
    menu_party_work_manage = (By.XPATH, '//div[text()="党务管理"]/parent::div[@class="header-menu-item-box"]')  # 党务管理
    menu_assistant_decision = (By.XPATH, '//div[text()="辅助决策"]/parent::div[@class="header-menu-item-box"]')  # 辅助决策
    menu_email = (By.XPATH, '//div[text()="内部邮件"]/parent::div[@class="header-menu-item-box"]')  # 内部邮件
    menu_student_forum = (By.XPATH, '//div[text()="学员论坛"]/parent::div[@class="header-menu-item-box"]')  # 学员论坛
    username = (By.XPATH, '//div[@class="username"]')  # 登录用户名

    def searchClass(self):
        """
        搜索班次
        """
        pass
        # frame = self.find_element_by(self.iframe1)
        # self.switch_to.frame(frame)
        # self.switch_to.frame('iframe7')
        # self.input_send_keys(self.searchInput, '测试')
        # self.element_click(self.searchBtn)