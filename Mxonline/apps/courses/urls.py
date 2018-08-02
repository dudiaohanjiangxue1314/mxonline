#encoding:utf-8
__author__ = 'mtianyan'
__date__ = '2018/8/1 16:44'

from courses.views import CourseListView
from django.urls import path,re_path

app_name = "courses"
urlpatterns = [
    # 课程列表url
    path('list/', CourseListView.as_view(), name="list"),


]







