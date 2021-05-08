from django.db import models

# Create your models here.


class Menu(models.Model):
    MENU_TYPE = (
        (1, "一级类目"),
        (2, "二级类目")
    )

    authName = models.CharField(max_length=40, blank=False, null=False, verbose_name="菜单名")
    path = models.CharField(max_length=255, blank=True, null=True, default='',verbose_name='路径')
    menu_type = models.IntegerField(choices=MENU_TYPE, default=1, help_text="类目级别")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="sub_cat", null=True, blank=True)  # 这里一定要有一个related_name，不然会报错

    class Meta:
        verbose_name = '导航菜单表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.authName

    # def validate_parent(self):
    #     pass


class Permission(models.Model):
    """
    权限基础信息表
    """
    per_name = models.CharField('权限名称', max_length=255, blank=False, null=False)
    path = models.CharField('权限路径', max_length=255, blank=True, null=True)
    level = models.IntegerField('权限级别', blank=False, null=False, default=1)
    # role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=False, null=False, name="不能没有隶属的权限")
    children = models.ForeignKey('self', on_delete=models.CASCADE,related_name='sub_cat',blank=True, null=True)

    class Meta:
        db_table='permission'
        verbose_name = "权限基础信息列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.per_name