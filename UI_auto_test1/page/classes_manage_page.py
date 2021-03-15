from selenium.webdriver.common.by import By

from common.base_page import BasePage


class ClassesManagePage(BasePage):
    """��ι���"""
    url = 'dsfa/teas/jwgl/bjgl/views/bclistzh.html'
    frame = (By.XPATH, '//iframe[@src="/dsfa/teas/jwgl/bjgl/views/bclistzh.html"]')
    frame_current = {'name': 'iframe7'}  # ��ǰ���frame
    frame_not_start = {'name': 'iframe11'}  # δ��ʼ���frame
    frame_history = {'name': 'iframe9'}  # ��ʷ���frame
    current_classes = (By.XPATH, '//font[text()="��ǰ���"]/parent::font/parent::li')  # ��ǰ���tab
    not_start_classes = (By.XPATH, '//font[text()="δ��ʼ���"]/parent::font/parent::li')  # δ��ʼ���tab
    history_classes = (By.XPATH, '//font[text()="��ʷ���"]/parent::font/parent::li')  # ��ʷ���tab
    search_input = '//div[@caption="classManageGrid"]//input[@placeholder="�������"]'  # ������������
    search_btn = '//div[@caption="classManageGrid"]//button[@class="layui-btn"]'  # ���������ť
    add_classes_btn = '//a[@class="ds_button  "]'  # ��Ӱ�ΰ�ť
    classes_num = '//span[@class="layui-laypage-count"]'  # �����Ϣ����1
