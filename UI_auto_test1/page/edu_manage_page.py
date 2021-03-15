from selenium.webdriver.common.by import By

from common.base_page import BasePage


class EduManagePage(BasePage):
    """�������"""
    url = ''
    submenu_classes_manage = (By.XPATH, '//div//span[@class="ds-aside-menu-item-name" and text()="��ι���"]')  # ��ι���
    submenu_teaching_manage = (By.XPATH, '//span[text()="��ѧ����"]/parent::div')  # ��ѧ����
    week_Timetable = (
        By.XPATH, '//font[text()="һ�ܿα�"]/ancestor::div[@class="ds-aside-menu-item-box"]')  # һ�ܿα�
    teach_plan = (By.XPATH, '//font[text()="��ѧ�ƻ�"]/ancestor::div[@class="ds-aside-menu-item-box"]')  # ��ѧ�ƻ�
    class_arrangement = (
        By.XPATH, '//font[text()="�ſι���"]/ancestor::div[@class="ds-aside-menu-item-box"]')  # �ſι���
    transferring_classes = (
        By.XPATH, '//font[text()="���μ�¼"]/ancestor::div[@class="ds-aside-menu-item-box"]')  # ���μ�¼
    submenu_task_manage = (By.XPATH, '//span[text()="��ҵ����"]/parent::div[@style="padding-left: 20px;"]')  # ��ҵ����
    task_manage = (By.XPATH, '//font[text()="��ҵ����"]/ancestor::li[@class="ds-aside-menu-item"]/div')  # ��ҵ����
    task_Review = (By.XPATH, '//font[text()="��ҵ����"]/ancestor::div[@class="ds-aside-menu-item-box"]')  # ��ҵ����
    results_registration = (By.XPATH, '//font[text()="�ɼ��Ǽ�"]/ancestor::div[@class="ds-aside-menu-item-box"]')  # �ɼ��Ǽ�
    submenu_notice_manage = (By.XPATH, '//span[text()="֪ͨ����"]/parent::div')  # ֪ͨ����
    submenu_teaching_evaluation_manage = (By.XPATH, '//span[text()="��ѧ���۹���"]/parent::div')  # ��ѧ���۹���
    submenu_teaching_data = (By.XPATH, '//span[text()="��ѧ����"]/parent::div')  # ��ѧ����
    submenu_certificate_print = (By.XPATH, '//span[text()="֤���ӡ"]/parent::div')  # ֤���ӡ
    submenu_my_schedule = (By.XPATH, '//span[text()="�ҵĿα�"]/parent::div')  # �ҵĿα�
    submenu_student_info = (By.XPATH, '//span[text()="ѧԱ��Ϣ��ѯ"]/parent::div')  # ѧԱ��Ϣ��ѯ
    submenu_teaching_set = (By.XPATH, '//span[text()="��ѧ����"]/parent::div')  # ��ѧ����
