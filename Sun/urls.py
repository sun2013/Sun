"""Sun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.views.static import serve
from Sun.settings import MEDIA_ROOT
from user.views import IndexView, UserArticleCategoryView, LoginView, RegisterView, ForgetView, ActiveUserView, ResetUserView, ModifyPwdView, RefreshCaptchaView
import xadmin

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    path('', IndexView.as_view(), name="index"),
    # 基于类方法实现登录,这里是调用它的方法
    path('login/', LoginView.as_view(), name="login"),
    # 基于类方法实现注册,这里是调用它的方法
    path('register/', RegisterView.as_view(), name="register"),
    # 基于类方法实现找回密码,这里是调用它的方法
    path('forget/', ForgetView.as_view(), name="forget"),
    # 验证码
    path("captcha/", include('captcha.urls')),
    # 刷新验证码
    path("getCaptcha/", RefreshCaptchaView.as_view(), name="refresh_captcha"),
    # 激活注册链接
    re_path('active/(?P<active_code>.*)', ActiveUserView.as_view(), name="user_active"),
    re_path('reset/(?P<active_code>.*)', ResetUserView.as_view(), name="user_reset"),
    path('modifypwd/', ModifyPwdView.as_view(), name='modifypwd'),
    path('selectArticleCategory/', UserArticleCategoryView.as_view(), name='user_article_category'),
]

