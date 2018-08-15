from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.views.generic.base import View
from django.contrib.auth.backends import ModelBackend
from django.core import serializers
from django.http import JsonResponse
from .models import UserArticleCategory, UserProfile, EmailVerifyRecord
from .forms import LoginForm, ForgetForm, RegisterForm
# 并集运算
from django.db.models import Q
# 实现用户名邮箱均可登录
# 继承ModelBackend类，因为它有方法authenticate，可点进源码查看
from utils.email_send import send_register_eamil


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self, raw_password):

            if user.check_password(password):
                return user
        except Exception as e:
            return None


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # 类实例化需要一个字典参数dict:request.POST就是一个QueryDict所以直接传入
        # POST中的usernamepassword，会对应到form中
        login_form = LoginForm(request.POST)
        # is_valid判断我们字段是否有错执行我们原有逻辑，验证失败跳回login页面

        if login_form.is_valid():
            # 取不到时为空，username，password为前端页面name值
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            # 成功返回user对象,失败返回null
            user = authenticate(username=user_name, password=pass_word)

            if user is not None:
                if user.is_active:
                    # login_in 两参数：request, user
                    # 实际是对request写了一部分东西进去，然后在render的时候：
                    # request是要render回去的。这些信息也就随着返回浏览器。完成登录
                    login(request, user)
                    # 登陆成功信息返回
                    return JsonResponse({"msg": "登陆成功", 'code': 200}, safe=False)
                else:
                    return JsonResponse({"msg": "用户未激活", 'code': 202}, safe=False)
            else:
                return JsonResponse({"msg": "用户名或者密码错误", 'code': 202}, safe=False)

        else:
            return JsonResponse({"msg": "老铁，认真填呀！你这样永远都不可能进去的呀~", 'code': 202}, safe=False)


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                return render(request, 'login.html')
        else:
            return render(request, 'user/active_fail.html')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # 取不到时为空，username，password为前端页面name值
            user_name = request.POST.get("email", "")
            users = UserProfile.objects.filter(email=user_name)
            if users:
                if users[0].is_active:
                    return JsonResponse({'code': 202, 'msg': '该邮箱已被注册'})
                else:
                    return JsonResponse({'code': 202, 'msg': '该邮箱已被注册,但是未激活，请去邮箱查看激活链接'})
            pass_word = request.POST.get("password", "")
            nick_name = request.POST.get("nick_name", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.nick_name = nick_name
            user_profile.password = make_password(pass_word)
            user_profile.is_active = False
            user_profile.save()
            send_status = send_register_eamil(user_name, "register")
            if send_status:
                return JsonResponse({'code': 200, 'msg': '激活邮件发送成功，请注意查收'})
            else:
                return JsonResponse({'code': 202, 'msg': '激活邮件发送失败'})
        else:
            return JsonResponse({'msg': register_form.errors, 'code': 202})


class ForgetView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forget.html', {'forget_form': forget_form})


class UserArticleCategoryView(View):
    def get(self, request):
        user_id = request.GET.get('user_id', '')
        category = serializers.serialize("json", UserArticleCategory.objects.filter(user_id=int(user_id)))
        # 判断是否存在，输出
        if category:
            return JsonResponse({'category': category})
