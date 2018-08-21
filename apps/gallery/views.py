from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
import json
from django.views.generic.base import View
from .models import GalleryCategory, GalleryBanner, GalleryImage, Gallery
# Create your views here.


class GalleryListView(View):
    def get(self, request):
        categorys = GalleryCategory.objects.all()
        banners = GalleryBanner.objects.all()
        return render(request, 'gallery/gallery.html', {
            'categorys': categorys,
            'banners': banners
        })
    
    def post(self, request):
        """
        type: 0 推荐 1 热门 2 最新
        :param request:
        :return:
        """
        type = request.POST.get('type', '')
        if type:
            if int(type) == 0:
                gallery_list = Gallery.objects.order_by('likes_nums')
            if int(type) == 1:
                gallery_list = Gallery.objects.order_by('click_nums')
            if int(type) == 2:
                gallery_list = Gallery.objects.order_by('release_time')
            gallery_list = serializers.serialize('json', gallery_list)
            gallery_list = json.loads(gallery_list)
            return JsonResponse({'msg': 'success', 'code': 200, 'data': gallery_list})
        else:
            return JsonResponse({'msg': 'fail', 'code': 202, 'data': ''})


class GalleryDetailView(View):
    def get(self, request, gallery_id):
        categorys = GalleryCategory.objects.all()
        gallery = Gallery.objects.get(id=int(gallery_id))
        tags = gallery.tags.split(',')
        gallery_images = gallery.galleryimage_set.all()
        return render(request, 'gallery/detail.html', {
            'categorys': categorys,
            'gallery': gallery,
            'tags': tags,
            'gallery_images': gallery_images
        })