# encoding=utf-8

"""
============================
Author:何超
Time:2021/3/1   17:30
============================
"""
import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import requests
from common.conf import conf
from PIL import Image
import pytesseract
import win32com.client

from common.path import common_dir, other_dir


class BasePage:
    """基础的页面类，封装一些页面中通用的操作方法"""
    _url = conf('env', 'host') + 'dsfa/teas/cms/views/login.html'

    def __init__(self, driver: WebDriver = None):
        """初始化driver"""
        if driver:
            self._driver = driver
        else:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(5)
            self._driver.maximize_window()
            self._driver.get(self._url)

    def find_element_by(self, loc):
        return self._driver.find_element(*loc)

    def find_elements_by(self, loc):
        return self._driver.find_elements(*loc)

    def get_cookie(self, username=conf("api_login", "superuser"), password=conf("api_login", "superpsw"), code='good',
                   loginType=8):
        data = {"loginName": username,
                "password": password,
                "code": code,
                "loginType": loginType
                }
        re = requests.request(method='POST', data=data, url=os.path.join(conf('env', 'host'), conf('url_api', 'login')))
        cookie = re.headers['Set-Cookie']
        list = cookie.split('=', 1)
        name = list[0]
        value = list[1].split(';', 1)[0]
        cookie = {'name': name, 'value': value}
        return cookie

    def open_browser(self, url):
        '''
        最大化浏览器并访问网址@
        :param url:访问的网址
        :return:
        '''
        self._driver.maximize_window()
        self._driver.get(url)

    def open_browser_no_login(self, url):
        '''
        最大化浏览器并访问网址,无需登录
        :param url:访问的网址
        :return:
        '''
        self._driver.get(url)
        self._driver.add_cookie(self.get_cookie())
        self._driver.refresh()
        time.sleep(2)

    def close_browser(self):
        '''
        关闭浏览器
        :return:
        '''
        self._driver.quit()

    def input_send_keys(self, loc, value, loc_desc=''):
        """
        input元素中输入数据
        :param loc: 元素的定位器 -->:(BY.xxx,'表达式')
        :param value: 输入的数据
        :param loc_desc: 元素文本的描述
        :return:
        """
        ele = self.find_element_by(loc)
        ele.clear()
        ele.send_keys(value)

    def element_click(self, loc, loc_desc=''):
        """
        点击元素
        :param loc: 元素的定位器 -->:(BY.xxx,'表达式')
        :param loc_desc: 元素文本的描述
        :return:
        """
        self.find_element_by(loc).click()

    def wait_visibility_ele(self, loc, loc_desc='', timeout=20, poll_time=0.5):
        """
        等待元素可见
        :param loc:元素的定位器 -->:(BY.xxx,'表达式')
        :param loc_desc:元素文本的描述
        :param timeout: 最大等待事件
        :param poll_time: 等待的轮询间隔
        :return: 定位到的元素
        """
        ele = WebDriverWait(self._driver, timeout, poll_time).until(EC.visibility_of_element_located(loc))
        return ele

    def wait_ele_be_click(self, loc, loc_desc='', timeout=20, poll_time=0.5):
        """
        等待元素可点击
        :param loc:元素的定位器 -->:(BY.xxx,'表达式')
        :param loc_desc:元素文本的描述
        :param timeout: 最大等待事件
        :param poll_time: 等待的轮询间隔
        :return: 定位到的元素
        """
        ele = WebDriverWait(self._driver, timeout, poll_time).until(EC.element_to_be_clickable(loc))
        return ele

    def get_ele_text(self, loc, loc_desc=''):
        """
        获取元素本文信息
        :param loc:元素的定位器 -->:(BY.xxx,'表达式')
        :param loc_desc:元素文本的描述
        :return: 元素文本信息
        """
        return self.find_element_by(loc).text

    def get_ele_attr(self, loc, attr, loc_desc=''):
        """
        获取元素本文信息
        :param loc:元素的定位器 -->:(BY.xxx,'表达式')
        :param attr:元素的属性名
        :param loc_desc:元素文本的描述
        :return: 元素属性
        """
        return self.find_element_by(*loc).get_attribute(attr)

    def switch_to_frame(self, loc='', frame_name='', frame_id=''):
        """
        切换frame框架
        :param loc:frame元素的定位器 -->:(BY.xxx,'表达式')
        :param frame_name:frame元素的name
        :param frame_id:frame元素的id
        :return:
        """
        if loc:
            frame = self._driver.find_element(*loc)
            self._driver.switch_to.frame(frame)
        elif frame_name:
            self._driver.switch_to.frame(frame_name)
        elif frame_id:
            self._driver.switch_to.frame(frame_id)
        else:
            raise Exception

    def switch_to_frame_back(self):
        """
        切换回到默认的内容范围
        :return:
        """
        self._driver.switch_to.default_content()

    def select_option_by_value(self, loc, index='', value='', text=''):
        """
        选择下拉框选项@未调试！！！！
        :param loc: 元素的定位器 -->:(BY.xxx,'表达式')
        :param value: 下拉选项的文本信息
        :return:
        """
        ele = self._driver.find_element(*loc)
        s = Select(ele)
        if index:
            s.select_by_index(value)
        elif value:
            s.select_by_value(value)
        elif text:
            s.select_by_visible_text(text)
        else:
            raise Exception

    def switch_to_handle(self, index=1):
        """
        跳转至新打开的标签页
        :param index: 标签页的句柄索引
        :return: 新打开的标签页面的标题
        """
        handles = self._driver.window_handles
        self._driver.switch_to.window(handles[index])
        return self._driver.title

    def get_pic_code(self, loc):
        """
        获取验证码图片的验证码
        :param url: 页面url
        :param loc: 验证码图片元素的定位器 -->:(BY.xxx,'表达式')
        :return: 验证码
        """
        pic_name = os.path.join(other_dir, 'screenshot_login_pic.png')
        self._driver.save_screenshot(pic_name)
        code = self._driver.find_element(*loc)
        left = code.location['x']
        top = code.location['y']
        right = code.size['width'] + left
        height = code.size['height'] + top
        im = Image.open(pic_name)
        img = im.crop((left, top, right, height))
        new_pic = os.path.join(other_dir, 'screenshot_login_code_pic.png')
        img.save(new_pic)
        img2 = Image.open(new_pic)
        text = pytesseract.image_to_string(img2)
        code_list = [i for i in text][0:4]
        code = ''.join(code_list)
        print(code)
        return code

    def move_to_ele(self, loc):
        """
        移动滚动条，使页面可见指定元素
        :param loc: 元素的定位器 -->:(BY.xxx,'表达式')
        :return:
        """
        ele = self._driver.find_element(*loc)
        self._driver.execute_script("arguments[0].scrollIntoView();", ele)

    def Mouse_hover_to_ele(self, loc):
        """
        鼠标悬停到指定元素位置
        :param loc: 元素的定位器 -->:(BY.xxx,'表达式')
        :return:
        """
        ele = self._driver.find_element(*loc)
        ActionChains(self._driver).move_to_element(ele).perform()

    @staticmethod
    def chang_mobile(device_name="Pixel 2"):
        """
        用手机模式打开浏览器
        :param device_name:设备名称
        :return:option
        """
        option = webdriver.ChromeOptions()
        mobile_emulation = {"deviceName": device_name}
        option.add_experimental_option("mobileEmulation", mobile_emulation)
        option.add_argument("--auto-open-devtools-for-tabs")
        return option

    @staticmethod
    def upload(filepath, exe_path=os.path.join(common_dir, 'upload.exe'), windows_class="[CLASS:#32770]",
               windows_title="打开", control_id_edit="Edit1", control_id_btn="Button1", wait_time="5000"):
        """
        上传文件:使用AutoIt工具辅助，调用exe脚本执行上传操作实现
        :param filepath:需要上传文件的路径
        :param exe_path: AutoIt脚本执行文件路径（输入上传文件路径->点击上传）
        :param windows_class:windows上传控件的class
        :param windows_title:windows上传控件的title
        :param control_id_edit:windows上传控件的输入框id
        :param control_id_btn:windows上传控件的上传按钮id
        :param wait_time:上传文件超时时间
        :return:
        """
        script = '{0} {1} {2} {3} {4} {5} {6}'.format(exe_path, filepath, windows_class, windows_title, control_id_edit,
                                                      control_id_btn, wait_time)
        os.system(script)

    @staticmethod
    def upload2(filepath):
        """
        上传文件：调用pywin32的Sendkeys实现，可能不太稳定
        :param filepath:上传文件路径
        :return:
        """
        time.sleep(1)
        shell = win32com.client.Dispatch("WScript.Shell")
        str = '{}{}\n'.format(filepath, '{ENTER}')
        shell.Sendkeys(str)
        time.sleep(1)


if __name__ == 'main':
    a = os.path.join(common_dir, 'upload.exe')
    print(a)
