from django.shortcuts import render
from django.views.generic.base import View
from .models import GalleryCategory, GalleryBanner
# Create your views here.


class GalleryListView(View):
    def get(self, request):
        categorys = GalleryCategory.objects.all()
        banners = GalleryBanner.objects.all()
        return render(request, 'gallery/gallery.html', {
            'categorys': categorys,
            'banners': banners
        })


class GalleryDetailView(View):
    def get(self, request, gallery_id):

        return render(request, 'gallery/detail.html')