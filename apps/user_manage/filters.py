import django_filters
from .models import SysUser


# class UserFilter(django_filters.rest_framework.FilterSet):
#     role = django_filters.CharFilter(name="role__name")
#
#     class Meta:
#         model = SysUser
#         fields = ['username', 'role']
