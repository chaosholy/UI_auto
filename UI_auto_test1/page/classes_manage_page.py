from selenium.webdriver.common.by import By

from common.base_page import BasePage


class ClassesManagePage(BasePage):
    """班次管理"""
    url = 'dsfa/teas/jwgl/bjgl/views/bclistzh.html'
    frame = (By.XPATH, '//iframe[@src="/dsfa/teas/jwgl/bjgl/views/bclistzh.html"]')
    frame_current = {'name': 'iframe7'}  # 当前班次frame
    frame_not_start = {'name': 'iframe11'}  # 未开始班次frame
    frame_history = {'name': 'iframe9'}  # 历史班次frame
    current_classes = (By.XPATH, '//font[text()="当前班次"]/parent::font/parent::li')  # 当前班次tab
    not_start_classes = (By.XPATH, '//font[text()="未开始班次"]/parent::font/parent::li')  # 未开始班次tab
    history_classes = (By.XPATH, '//font[text()="历史班次"]/parent::font/parent::li')  # 历史班次tab
    search_input = '//div[@caption="classManageGrid"]//input[@placeholder="班次名称"]'  # 班次搜索输入框
    search_btn = '//div[@caption="classManageGrid"]//button[@class="layui-btn"]'  # 班次搜索按钮
    add_classes_btn = '//a[@class="ds_button  "]'  # 添加班次按钮
    classes_num = '//span[@class="layui-laypage-count"]'  # 班次信息条数1
