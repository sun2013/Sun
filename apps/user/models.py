from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    # 自定义的性别选择规则
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )
    # 昵称
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    # 生日，可以为空
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    # 性别 只能男或女，默认女
    gender = models.CharField(
        max_length=10,
        verbose_name=u"性别",
        choices=GENDER_CHOICES,
        default="female")
    # 地址
    address = models.CharField(max_length=100, verbose_name="地址", default="")
    # 电话
    mobile = models.CharField(max_length=11, null=True, blank=True)
    # 头像 默认使用default.png
    image = models.ImageField(
        upload_to="avatar/%Y/%m",
        default=u"avatar/default.png",
        max_length=100,
        blank = True
    )

    # meta信息，即后台栏目名
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 重载Unicode方法，打印实例会打印username，username为继承自abstractuser
    def __str__(self):
        return self.username


# 邮箱验证码model


class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ("register", u"注册"),
        ("forget", u"找回密码")
    )
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    # 未设置null = true blank = true 默认不可为空
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(choices=SEND_CHOICES, max_length=10)
    is_active = models.BooleanField(default=False, verbose_name="是否被使用过")
    # 这里的now得去掉(),不去掉会根据编译时间。而不是根据实例化时间。
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


# 轮播图model


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(
        upload_to="banner/%Y/%m",
        verbose_name=u"轮播图",
        blank=True,
        max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    # 默认index很大靠后。想要靠前修改index值。
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 用户等级


class UserGrade(models.Model):
    level_num = models.IntegerField(default=0, verbose_name="等级")
    level_name = models.CharField(max_length=20, verbose_name="用户等级名称")
    level_exp = models.IntegerField(default=0, verbose_name="等级经验")

    class Meta:
        verbose_name = u"用户等级"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.level_name


# 用户说说


class UserMood(models.Model):
    desc = models.TextField(verbose_name="说说详情")
    images = models.TextField(verbose_name="图片内容", default="", blank=True, null=True)
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    click_nums = models.IntegerField(default=0, verbose_name=u"点赞人数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户说说"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.desc


# 用户日志类型


class UserArticleCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="日志分组名称")
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户日志类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 用户日志


class UserArticle(models.Model):
    title = models.CharField(verbose_name="标题", max_length=200)
    desc = models.TextField(verbose_name="日志简述")
    detail = models.TextField(verbose_name="文章详情")
    image = models.ImageField(upload_to="article/%Y/%m", verbose_name=u"封面图", blank=True, max_length=100)
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE, default="")
    category = models.ForeignKey(UserArticleCategory, verbose_name="日志类型", on_delete=models.CASCADE)
    click_nums = models.IntegerField(default=0, verbose_name="点赞人数")
    view_nums = models.IntegerField(default=0, verbose_name="浏览人数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户日志"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

