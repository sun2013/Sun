"""
@author: sun
@file: urls.py
@time: 2018/8/20 13:51
@desc:
"""
from django.urls import path, re_path, include
from .views import GalleryListView, GalleryDetailView

app_name = "gallery"
urlpatterns = [
    path('list/', GalleryListView.as_view(), name="list"),
    re_path('detail/(?P<gallery_id>.*)/', GalleryDetailView.as_view(), name="detail"),
]