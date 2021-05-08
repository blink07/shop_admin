import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from menu.models import Permission


class Role(models.Model):
    """
    角色表
    """
    role_no = models.IntegerField("角色编号",blank=False, null=False, default=3)
    role_name = models.CharField("角色名称",max_length=20, blank=False, null=False, default="访问角色")
    role_descripte = models.CharField('角色描述', max_length=100, blank=False, null=False, default='游客')
    status = models.IntegerField("状态", blank=False, null=False, default=1)
    show_no = models.IntegerField("角色显示顺序", blank=False, null=False, default=100)
    create_time = models.DateField("创建时间", blank=False, null=False, default=datetime.datetime.now)

    class Meta:
        db_table = "user_role"
        verbose_name = "用户角色"
        verbose_name_plural=verbose_name

    # def __str__(self):
    #     return self.role_name


class PermissionRole(models.Model):
    """
    权限-角色表
    """
    per_name = models.CharField('权限名称', max_length=255, blank=False, null=False)
    path = models.CharField('权限路径', max_length=255, blank=False, null=False)
    level = models.IntegerField('权限级别', blank=False, null=False, default=1)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='permissions',blank=False, null=False, verbose_name="权限必须分配给角色")
    children = models.ForeignKey('self', on_delete=models.CASCADE,related_name='permission_children',blank=True, null=True)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, related_name='per_permission', blank=False, null=False, default=1)

    class Meta:
        db_table='permission_role'
        verbose_name = "权限角色列表"
        verbose_name_plural = verbose_name

    # def __str__(self):
    #     return self.per_name


class Department(models.Model):
    """
    部门表
    """
    dept_no = models.IntegerField("部门编号",blank=False, null=False)
    dept_name = models.CharField("部门名称", max_length=100, blank=False, null=False, default='')
    charge_person = models.CharField("负责人", max_length=10, blank=False, null=False, default= '')
    email = models.EmailField("邮箱地址", blank=True)
    show_no = models.IntegerField("显示排序",blank=True, null=False,default=10)
    tel = models.CharField("联系电话", max_length=11, blank=True, null=False, default='')
    status = models.IntegerField("部门状态", blank=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="上级部门", blank=True, null=True)

    class Meta:
        db_table = 'department'
        verbose_name = '部门信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.dept_name


class SysUser(AbstractUser):
    """
    用户表
    """

    GENDER_CHOICE = (
        ("male", u"男"),
        ("female", u"女")
    )
    mobile = models.CharField("手机号码", max_length=11, blank=False, null=False)
    gender = models.CharField("性别", max_length=6, choices=GENDER_CHOICE, default="male")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=False, null=False, default=1)
    avatar = models.CharField("头像", max_length=255, blank=True, null=True)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    state = models.BooleanField(default=True, blank=True, null=True)
    # address = models.CharField("地址", max_length=255, blank=True, null=True)  # 还未同步到数据库

    class Meta:
        db_table = 'sys_user'
        verbose_name = '系统用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username







