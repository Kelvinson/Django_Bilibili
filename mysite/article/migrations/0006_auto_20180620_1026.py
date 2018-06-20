# Generated by Django 2.0.6 on 2018-06-20 02:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20180620_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='article',
            name='context',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='article',
            name='last_update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='上次修改时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='read_num',
            field=models.IntegerField(default=0, verbose_name='阅读次数'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tittle',
            field=models.CharField(max_length=30, verbose_name='标题'),
        ),
    ]