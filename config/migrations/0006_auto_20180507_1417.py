# Generated by Django 2.0.5 on 2018-05-07 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_auto_20180507_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sidebar',
            options={'ordering': ('-display_type',), 'verbose_name': '侧边栏', 'verbose_name_plural': '侧边栏'},
        ),
    ]
