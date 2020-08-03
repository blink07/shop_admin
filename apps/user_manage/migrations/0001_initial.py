# Generated by Django 3.0.5 on 2020-07-04 09:25

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_no', models.IntegerField(default=3, verbose_name='角色编号')),
                ('role_name', models.CharField(default='访问角色', max_length=20, verbose_name='角色名称')),
                ('role_descripte', models.CharField(default='游客', max_length=100, verbose_name='角色描述')),
                ('status', models.IntegerField(default=1, verbose_name='状态')),
                ('show_no', models.IntegerField(default=100, verbose_name='角色显示顺序')),
                ('create_time', models.DateField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户角色',
                'verbose_name_plural': '用户角色',
                'db_table': 'user_role',
            },
        ),
        migrations.CreateModel(
            name='PermissionRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_name', models.CharField(max_length=255, verbose_name='权限名称')),
                ('path', models.CharField(blank=True, max_length=255, verbose_name='权限路径')),
                ('level', models.IntegerField(default=1, verbose_name='权限级别')),
                ('children', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_manage.PermissionRole')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_manage.Role', verbose_name='权限必须分配给角色')),
            ],
            options={
                'verbose_name': '权限角色列表',
                'verbose_name_plural': '权限角色列表',
                'db_table': 'permission_role',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per_name', models.CharField(max_length=255, verbose_name='权限名称')),
                ('path', models.CharField(blank=True, max_length=255, null=True, verbose_name='权限路径')),
                ('level', models.IntegerField(default=1, verbose_name='权限级别')),
                ('children', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_manage.Permission')),
            ],
            options={
                'verbose_name': '权限基础信息列表',
                'verbose_name_plural': '权限基础信息列表',
                'db_table': 'permission',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_no', models.IntegerField(verbose_name='部门编号')),
                ('dept_name', models.CharField(default='', max_length=100, verbose_name='部门名称')),
                ('charge_person', models.CharField(default='', max_length=10, verbose_name='负责人')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='邮箱地址')),
                ('show_no', models.IntegerField(blank=True, default=10, verbose_name='显示排序')),
                ('tel', models.CharField(blank=True, default='', max_length=11, verbose_name='联系电话')),
                ('status', models.IntegerField(blank=True, verbose_name='部门状态')),
                ('parent_comment', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user_manage.Department', verbose_name='上级部门')),
            ],
            options={
                'verbose_name': '部门信息',
                'verbose_name_plural': '部门信息',
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='SysUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号码')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=6, verbose_name='性别')),
                ('avatar', models.CharField(blank=True, max_length=255, null=True, verbose_name='头像')),
                ('state', models.BooleanField(blank=True, default=True, null=True)),
                ('dept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_manage.Department')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('role', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_manage.Role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '系统用户',
                'verbose_name_plural': '系统用户',
                'db_table': 'sys_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
