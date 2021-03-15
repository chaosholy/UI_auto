# encoding=utf-8
import os
import time

from selenium.webdriver import Chrome, ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.base_page import BasePage
from common.path import caseData_dir

"""
调试用脚本，
chrome路径
C:\Program Files\Google\Chrome\Application
cmd：
chrome --remote-debugging-port=9999
"""


def get_ele(loc, debugger_address="localhost:9999"):
    """
    调试元素定位
    :param loc:元素定位器 
    :return: 元素文本
    """""
    options = Options()
    options.debugger_address = debugger_address
    driver = webdriver.Chrome(options=options)
    frame = (By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/iframe')
    data = driver.find_element(*loc).text
    print(data)
    return data

def select_option_by_value(self, loc, index='', value='', text=''):
    """
    选择下拉框选项@未调试！！！！
    :param loc: 元素的定位器 -->:(BY.xxx,'表达式')
    :param value: 下拉选项的文本信息
    :return:
    """
    ele = self.driver.find_element(*loc)
    s = Select(ele)
    if index:
        s.select_by_index(value)
    elif value:
        s.select_by_value(value)
    elif text:
        s.select_by_visible_text(text)
    else:
        raise Exception

# ele = (By.CSS_SELECTOR, '.username')
# get_ele(ele)

options = Options()
options.debugger_address = "localhost:9999"
dr = webdriver.Chrome(options=options)

dr.implicitly_wait(5)
# try:
# time.sleep(1)
#移动鼠标悬停
dr.switch_to.frame('listxygl')
ele = dr.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[3]/div[3]/div/div/a[4]")
ActionChains(dr).move_to_element(ele).perform()

def Mouse_hover_to_ele(self,loc):
    ele = self.driver.find_element(*loc)
    ActionChains(self.driver).move_to_element(ele).perform()


