# Generated by Django 3.2.13 on 2022-05-20 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0004_userstaff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detailuser',
            options={'verbose_name': 'اطلاعات کاربر', 'verbose_name_plural': 'اطلاعات کاربران'},
        ),
        migrations.AlterModelOptions(
            name='userstaff',
            options={'verbose_name': 'اطلاعات کارمند', 'verbose_name_plural': 'اطلاعات کارمندان'},
        ),
    ]
