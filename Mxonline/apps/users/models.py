from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    GENDER_CHOICE = (('male',u'男'),('female',u'女'))

    nick_name = models.CharField(max_length=50,verbose_name=u'昵称',default='')
    birthday = models.DateField(verbose_name=u'生日',null=True,blank=True)
    gender = models.CharField(max_length=6,verbose_name=u'性别',choices=GENDER_CHOICE,default='female')
    address = models.CharField(max_length=100,verbose_name=u'地址',default='')
    mobile = models.CharField(max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to='image/%Y/%m',default=u'image/default.png',max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username

class EmailVerifyRecord(models.Model):
    SEND_CHOICE = (
        ('register',u'注册'),
        ('forget',u'找回密码')
    )

    code = models.CharField(max_length=20,verbose_name=u'验证码')
    email = models.EmailField(max_length=50,verbose_name=u'邮箱')
    send_type = models.CharField(choices=SEND_CHOICE,max_length=10,verbose_name='发送类型')
    send_time = models.DateTimeField(default=datetime.now,verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name
    # 重载__str__方法使后台不再直接显示object
    def __str__(self):
        return '{0}({1})'.format(self.code,self.email)

class Banner(models.Model):
    title = models.CharField(max_length=100,verbose_name=u'标题')
    image = models.ImageField(
        upload_to='banner/%Y/%m',
        verbose_name=u'轮播图',
        max_length=100
    )
    url = models.URLField(max_length=200, verbose_name=u"访问地址")

    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
