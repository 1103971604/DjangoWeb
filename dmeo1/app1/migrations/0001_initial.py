# Generated by Django 2.2.1 on 2019-05-28 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img', models.ImageField(upload_to='Add', verbose_name='图片文件')),
                ('Message', models.CharField(max_length=20, verbose_name='消息')),
            ],
            options={
                'verbose_name': '轮播',
                'verbose_name_plural': '轮播',
            },
        ),
        migrations.CreateModel(
            name='CategroyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30, verbose_name='类型')),
            ],
            options={
                'verbose_name': '游戏类型',
                'verbose_name_plural': '游戏类型',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, verbose_name='用户名')),
                ('Email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮箱')),
                ('Phone', models.CharField(max_length=11, verbose_name='电话')),
                ('Message', tinymce.models.HTMLField(verbose_name='消息体')),
            ],
            options={
                'verbose_name': '反馈信息',
                'verbose_name_plural': '反馈信息',
            },
        ),
        migrations.CreateModel(
            name='GmaeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, verbose_name='游戏名')),
                ('Creat_Time', models.DateTimeField(auto_now_add=True, verbose_name='上传日期')),
                ('Update_Time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('Img', models.ImageField(upload_to='Game', verbose_name='图片')),
                ('Body', models.TextField(default='', max_length=1000, verbose_name='游戏介绍')),
                ('ReadNum', models.PositiveIntegerField(default=0, verbose_name='阅读数')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.CategroyInfo', verbose_name='游戏类型')),
            ],
            options={
                'verbose_name': '游戏信息',
                'verbose_name_plural': '游戏信息',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20, verbose_name='用户名')),
                ('Subject', models.CharField(max_length=30, verbose_name='题目')),
                ('Emali', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮箱')),
                ('Message', tinymce.models.HTMLField(verbose_name='消息体')),
                ('Game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.GmaeInfo', verbose_name='游戏名')),
            ],
            options={
                'verbose_name': '评论信息',
                'verbose_name_plural': '评论信息',
            },
        ),
    ]
