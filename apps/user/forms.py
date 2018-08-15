"""
@author: sun
@file: forms.py
@time: 2018/8/14 15:25
@desc:
"""
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # 用户名密码不能为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    nick_name = forms.CharField(required=True, max_length=24)
    password = forms.CharField(required=True, min_length=5)


