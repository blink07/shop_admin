# Generated by Django 3.1 on 2021-07-20 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_permission'),
        ('user_manage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permissionrole',
            name='permission',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='per_permission', to='menu.permission'),
        ),
        migrations.AlterField(
            model_name='department',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_manage.department', verbose_name='上级部门'),
        ),
        migrations.AlterField(
            model_name='permissionrole',
            name='children',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permission_children', to='user_manage.permissionrole'),
        ),
        migrations.AlterField(
            model_name='permissionrole',
            name='path',
            field=models.CharField(max_length=255, verbose_name='权限路径'),
        ),
        migrations.AlterField(
            model_name='permissionrole',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='permissions', to='user_manage.role', verbose_name='权限必须分配给角色'),
        ),
        migrations.AlterField(
            model_name='sysuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
    ]