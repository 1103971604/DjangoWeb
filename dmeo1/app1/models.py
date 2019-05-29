from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
# 游戏类型
class CategroyInfo(models.Model):
    Title=models.CharField(max_length=30,verbose_name='类型')

    class Meta():
        verbose_name = "游戏类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Title

# 游戏信息
class GmaeInfo(models.Model):
    Name=models.CharField(max_length=30,verbose_name='游戏名')
    Creat_Time=models.DateTimeField(auto_now_add=True,verbose_name='上传日期')
    Update_Time=models.DateTimeField(auto_now=True,verbose_name='更新日期')
    Img=models.ImageField(upload_to='Game',verbose_name='图片')
    Author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    Body=models.TextField(max_length=1000,default='',verbose_name='游戏介绍')
    ReadNum=models.PositiveIntegerField(default=0,verbose_name='阅读数')
    Category=models.ForeignKey(CategroyInfo,on_delete=models.CASCADE,verbose_name='游戏类型')

    class Meta():
        verbose_name = "游戏信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Name

# 反馈
class Feedback(models.Model):
    Name=models.CharField(max_length=30,verbose_name='用户名')
    Email=models.EmailField(blank=True,null=True,verbose_name='邮箱')
    Phone=models.CharField(max_length=11,verbose_name='电话')
    Message=HTMLField(verbose_name='消息体')

    def __str__(self):
        return self.Name

    class Meta():
        verbose_name = "反馈信息"
        verbose_name_plural = verbose_name

# 评论
class Comment(models.Model):
    Name=models.CharField(max_length=20,verbose_name='用户名')
    Subject=models.CharField(max_length=30,verbose_name='题目')
    Emali=models.EmailField(blank=True,null=True,verbose_name='邮箱')
    Message=HTMLField(verbose_name='消息体')
    Game=models.ForeignKey(GmaeInfo,on_delete=models.CASCADE,verbose_name='游戏名')

    def __str__(self):
        return self.Name

    class Meta():
        verbose_name = "评论信息"
        verbose_name_plural = verbose_name

class AddImg(models.Model):
    Img = models.ImageField(upload_to='Add', verbose_name='图片文件')
    Message = models.CharField(max_length=20, verbose_name='消息')

    class Meta():
        verbose_name = "轮播"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Message

