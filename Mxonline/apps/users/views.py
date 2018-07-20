#coding=utf-8

from django.shortcuts import render
from django.contrib.auth import  authenticate,login
from django.contrib.auth.backends import ModelBackend
from  .models import UserProfile
# 并集运算
from django.db.models import Q


# Create your views here.
# 实现用户名邮箱均可登录
# 继承ModelBackend类，因为它有方法authenticate，可点进源码查看
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询

            user = UserProfile.objects.get(Q(username=username)|Q(email=username))

            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self, raw_password):

            if user.check_password(password):
                return user
        except Exception as e:
            return None



def LoginView(request):

    # 登录提交表单为post
    if request.method == 'POST':
        # 取不到时为空，username，password为前端页面name值
        user_name = request.POST.get("username","")
        pass_word = request.POST.get('password','')

        # 成功返回user对象,失败返回None
        user = authenticate(username=user_name,password=pass_word)
        if user is not None:
            # login_in 两参数：request, user
            # 实际是对request写了一部分东西进去，然后在render的时候：
            # request是要render回去的。这些信息也就随着返回浏览器。完成登录
            login(request,user)
            # 跳转到首页 user request会被带回到首页
            return render(request,'index.html')
        # 没有成功说明里面的值是None，并再次跳转回主页面
        else:
            return render(request,'login.html',{'msg':'用户名或密码错误！'})
    elif request.method == 'GET':
        return render(request,'login.html',{})

