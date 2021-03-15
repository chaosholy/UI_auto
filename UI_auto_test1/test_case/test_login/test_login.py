# encoding=utf-8

import pytest
from page.home_page import HomePage
from page.login_page import LoginPage
import yaml
import allure


class TestLogin:
    """登录的测试用例类"""
    __data = yaml.safe_load(open('./login_data.yml'))

    def setup(self):
        self.run = LoginPage()

    def teardown(self):
        self.run.close_browser()

    @allure.feature("test_module_01")
    @pytest.mark.parametrize("username,password", __data["test_login_pass"])
    def test_login_pass(self, username, password):
        """
        验证登录成功
        """
        assert "超级管理员" in self.run.login_pass(username, password)
