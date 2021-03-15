# encoding=utf-8
from selenium import webdriver
import win32gui
import win32con
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.base_page import BasePage
import win32com.client
# import SendKeys
def upload2(filepath):
    """
    上传文件第二种方法
    :param filepath:上传文件路径
    :return:
    """
    time.sleep(1)
    shell = win32com.client.Dispatch("WScript.Shell")
    str = '{}{}\n'.format(filepath, '{ENTER}')
    shell.Sendkeys(str)
    time.sleep(1)



dr = webdriver.Chrome()
Base_Page = BasePage(dr)
Base_Page.open_browser_no_login('http://125.69.82.54:16101/dsf5/index.html')
dr.implicitly_wait(10)
dr.find_element(By.XPATH,'//*[@id="app"]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div/i').click()
btn = (By.XPATH,'//*[@id="app"]/div/div/div[2]/div[1]/div/div/div[1]/ul/li[6]/div')
Base_Page.element_click(btn)
frame = dr.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div/iframe')
dr.switch_to.frame(frame)
dr.switch_to.frame('iframe21')
ele =(By.XPATH,'//div[text()="橙子教学班"]/ancestor::tr[@class="ds_control no_padding ds_container"]//div[text()="上传"]/parent::a')
WebDriverWait(dr, 20, 0.5).until(EC.element_to_be_clickable(ele))
dr.find_element(*ele).click()
time.sleep(1)
a = r'C:\Users\Administrator\Desktop\1234.png'
BasePage.upload(a)
time.sleep(1)

dr.close()

