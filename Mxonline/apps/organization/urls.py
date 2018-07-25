#encoding:utf-8
from organization.views import OrgView,AddUserAskView
from django.urls import path ,re_path

__author__ = 'mtianyan'
__date__ = '2018/7/25 13:20'
app_name = "organization"
urlpatterns = [
    # 课程机构列表url
    path('list/', OrgView.as_view(), name="org_list"),
    # 添加我要学习
    path('add_ask/', AddUserAskView.as_view(), name="add_ask"),

]