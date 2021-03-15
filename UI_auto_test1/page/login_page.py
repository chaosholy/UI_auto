# encoding=utf-8

"""
============================
Author:何超
Time:2021/3/1   16:00
============================
"""

from selenium.webdriver.common.by import By
from common.conf import conf
from common.base_page import BasePage
from page.home_page import HomePage


class LoginPage(BasePage):
    """登录页面"""
    # url = 'dsfa/teas/cms/views/login.html'
    __loginName = (By.XPATH, '//input[@class="telNum" and @name = "loginName"]')
    __password = (By.XPATH, '//input[@class="telNum" and @name = "password"]')
    __code = (By.XPATH, '//input[@id="code"]')
    __loginBtn = (By.XPATH, '//h5[@class="jscenter" and text() = "登录"]')
    __failTips = (By.XPATH, '//div[@class="layui-layer-content layui-layer-padding"]')
    __code_btn = (By.XPATH, '//*[@id="userb"]/div[3]/div/img')
    __username = (By.CSS_SELECTOR, '.username')

    def login_pass(self, username, password, code='good'):
        """
         登录操作
        :param username: 登录名
        :param password: 密码
        :param code:验证码
        :return:
        """
        self.input_send_keys(self.__loginName, username)
        self.input_send_keys(self.__password, password)
        # code = self.get_pic_code(self.__code_btn)
        self.input_send_keys(self.__code, code)
        # self.driver.find_element(By.XPATH, '//h5[@class="jscenter" and text() = "登录"]').click()
        self.element_click(self.__loginBtn)
        # self.wait_visibility_ele(self.__username, timeout=5)
        return self.get_ele_text(self.__username)



    def goto_homepage(self, username, password, code='good'):
        self.input_send_keys(self.__loginName, username)
        self.input_send_keys(self.__password, password)
        code1 = self.get_pic_code(self.__code_btn)
        self.input_send_keys(self.__code, code1)
        self.element_click(self.__loginBtn)
        return HomePage(self)
    # def reset_login_page(self):
    #     """打开登录页面"""
    #     self.driver.get(conf('env', 'host') + 'dsfa/teas/cms/views/login.html')
