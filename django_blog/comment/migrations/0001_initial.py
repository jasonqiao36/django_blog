# Generated by Django 2.2.6 on 2019-10-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveIntegerField(choices=[(0, '删除'), (1, '正常'), (2, '草稿')], default=1, verbose_name='状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('target', models.CharField(max_length=200, null=True, verbose_name='评论目标')),
                ('nickname', models.CharField(max_length=64, verbose_name='用户名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('website', models.URLField(verbose_name='网站地址')),
                ('content', models.CharField(max_length=2000, verbose_name='内容')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
