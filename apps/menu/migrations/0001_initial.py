# Generated by Django 3.0.5 on 2020-07-04 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authName', models.CharField(max_length=40, verbose_name='菜单名')),
                ('path', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='路径')),
                ('menu_type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目')], default=1, help_text='类目级别')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='menu.Menu')),
            ],
            options={
                'verbose_name': '导航菜单表',
                'verbose_name_plural': '导航菜单表',
            },
        ),
    ]
