#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/11 16:05
# @Author  : Sun
# @File    : adminx.py


import xadmin
from .models import EmailVerifyRecord, Banner, UserGrade, UserMood, UserArticleCategory, UserArticle
from xadmin import views


# X admin的全局配置信息设置
class BaseSetting(object):
    # 主题功能开启
    enable_themes = True
    use_bootswatch = True

# x admin 全局配置参数信息设置


class GlobalSettings(object):
    site_title = "果实后台管理系统"
    site_footer = "sun's web"
    # 收起菜单
    menu_style = "accordion"



# 创建admin的管理类,这里不再是继承admin，而是继承object
class EmailVerifyRecordAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 配置筛选字段
    list_filter = ['code', 'email', 'send_type', 'send_time']


# 创建banner的管理类
class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


# 创建用户等级的管理类
class UserGradeAdmin(object):
    list_display = ['level_num', 'level_name', 'level_exp']
    search_fields = ['level_num', 'level_name', 'level_exp']
    list_filter = ['level_num', 'level_name', 'level_exp']


# 创建用户说说的管理类
class UserMoodAdmin(object):
    list_display = ['desc', 'images', 'click_nums', 'add_time']
    search_fields = ['desc', 'images', 'click_nums']
    list_filter = ['desc', 'images', 'click_nums', 'add_time']


# 创建日志类型的管理类
class UserArticleCategoryAdmin(object):
    list_display = ['name', 'user', 'add_time']
    search_fields = ['name', 'user']
    list_filter = ['name', 'user', 'add_time']


# 创建日志管理类
class UserArticleAdmin(object):
    list_display = ('title', 'desc', 'detail', 'image', 'category', 'click_nums', 'view_nums', 'add_time')
    search_fields = ['title', 'desc', 'detail', 'image', 'click_nums', 'view_nums']
    list_filter = ('title', 'desc', 'detail', 'image',  'click_nums', 'view_nums', 'add_time')


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(UserGrade, UserGradeAdmin)
xadmin.site.register(UserMood, UserMoodAdmin)
xadmin.site.register(UserArticleCategory, UserArticleCategoryAdmin)
xadmin.site.register(UserArticle, UserArticleAdmin)

# 将Xadmin全局管理器与我们的view绑定注册。
xadmin.site.register(views.BaseAdminView, BaseSetting)

# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView, GlobalSettings)