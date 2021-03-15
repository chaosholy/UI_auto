# encoding=utf-8

from common.conf import conf

login_pass_data = [
    {"title": "登录成功", 'username': conf('login', 'superuser'), 'password': conf('login', 'superpsw'),
     'expect': '欢迎您,超级管理员'}]

login_fail_by_error_username_or_psw = [
    {"title": "登录失败_错误账户", 'username': 'abcde', 'password': conf('login', 'superpsw'), 'expect': '您输入的账号或密码错误！'},
    {"title": "登录失败_错误密码", 'username': conf('login', 'superuser'), 'password': '123456', 'expect': '您输入的账号或密码错误！'},
    {"title": "登录失败_空账户", 'username': '', 'password': conf('login', 'superpsw'), 'expect': '请输入账号'},
    {"title": "登录失败_空密码", 'username': conf('login', 'superuser'), 'password': '', 'expect': '请输入密码1'}
]
