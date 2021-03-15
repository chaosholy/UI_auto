# encoding=utf-8

import os, sys

import pytest
from selenium.webdriver import Chrome
from selenium import webdriver
from page.login_page import LoginPage
from common.conf import conf

def create_driver():
    """打开浏览器 创建driver"""
    # if conf.conf1.getboolean('run', 'headless'):
    #     options = webdriver.ChromeOptions()
    #     options.add_argument('--headless')
    #     options.add_argument('--disable-gpu')
    #     driver = webdriver.Chrome(options=options)
    # else:
    driver = Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

# @pytest.fixture(scope='function')
# def login_setup():
#     """登录的前置方法"""
#     dr = create_driver()
#     url = conf('env', 'host') + 'dsfa/teas/cms/views/login.html'
#     dr.get(url)
#     login_page = LoginPage(dr)
#     yield login_page
#     dr.quit()
