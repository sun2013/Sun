from datetime import datetime
from django.db import models

# Create your models here.


class GalleryCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="分类名称")
    desc = models.CharField(max_length=100, verbose_name="分类描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"图片类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Gallery(models.Model):
    title = models.CharField(max_length=100, verbose_name="图片标题")
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, verbose_name='图片分类')
    release_time = models.CharField(max_length=50, verbose_name="发布时间")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击人数")
    likes_nums = models.IntegerField(default=0, verbose_name=u"点赞人数")
    tags = models.CharField(max_length=200, verbose_name="关键字")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "图片详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    image = models.ImageField(
        upload_to="gallery/",
        default="",
        max_length=100,
        blank=True
    )
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name='图片分类')

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = verbose_name


class GalleryBanner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(
        upload_to="banner/%Y/%m",
        verbose_name=u"图库轮播图",
        blank=True,
        max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    # 默认index很大靠后。想要靠前修改index值。
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"图库轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

