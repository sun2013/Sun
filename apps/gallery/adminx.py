"""
@author: sun
@file: adminx.py
@time: 2018/8/20 10:51
@desc:
"""
import xadmin
from .models import GalleryCategory, Gallery, GalleryImage, GalleryBanner


class GalleryCategoryAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['name', 'desc', 'add_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['name', 'desc']
    # 配置筛选字段
    list_filter = ['name', 'desc', 'add_time']


class GalleryImageAdmin(object):
    model = GalleryImage
    # 配置后台我们需要显示的列
    list_display = ['image', 'gallery']
    # 配置搜索字段,不做时间搜索
    search_fields = ['image', 'gallery']
    # 配置筛选字段
    list_filter = ['image', 'gallery']


class GalleryAdmin(object):
    inlines = [GalleryImageAdmin, ]
    # 配置后台我们需要显示的列
    list_display = ['title', 'category', 'tags', 'release_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['title', 'category', 'tags']
    # 配置筛选字段
    list_filter = ['title', 'category', 'tags', 'release_time']


# 创建banner的管理类
class GalleryBannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(Gallery, GalleryAdmin)
xadmin.site.register(GalleryCategory, GalleryCategoryAdmin)
xadmin.site.register(GalleryBanner, GalleryBannerAdmin)