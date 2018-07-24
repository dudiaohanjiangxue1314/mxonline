#coding=utf-8
from django.shortcuts import render
from django.views.generic.base import View
from .models import CourseOrg,CityDict
# Create your views here.


# 处理课程机构列表的view
class OrgView(View):
    def get(self,request):
        # 查找到所有的课程机构
        all_orgs = CourseOrg.objects.all()
        # 统计课程机构总数
        org_nums = all_orgs.count()
        # 取出所有的城市
        all_citys = CityDict.objects.all()

        return render(request, "org-list.html", {
            "all_orgs":all_orgs,
            "all_citys": all_citys,
            "org_nums":org_nums,
        })
