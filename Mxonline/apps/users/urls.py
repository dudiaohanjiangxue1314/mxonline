#encoding:utf-8
__author__ = 'mtianyan'
__date__ = '2018/8/7 16:24'
from django.urls import path ,re_path
from .views import UserInfoView,UploadImageView,UpdatePwdView,SendEmailCodeView,UpdateEmailView

app_name = "users"
urlpatterns = [
    # 用户信息
    path('info/', UserInfoView.as_view(), name="user_info"),
    # 用户头像上传
    path('image/upload/', UploadImageView.as_view(), name="image_upload"),
    # 用户个人中心修改密码
    path('update/pwd/', UpdatePwdView.as_view(), name="update_pwd"),
    # 专用于发送验证码的
    path('sendemail_code/', SendEmailCodeView.as_view(),name="sendemail_code"),
    # 修改邮箱
    path('update_email/', UpdateEmailView.as_view(), name="update_email"),


]