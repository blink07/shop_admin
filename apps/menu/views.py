from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from menu.models import Menu, Permission
from menu.serializers import MenuSerializer, PermissionSerializer, \
    PermissionSerializer3
from utils.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin


class MenuViewSet(ListModelMixin,CreateModelMixin,viewsets.GenericViewSet):
    """
    获取导航菜单栏
    ### Menu模块的新增菜单接口127.0.0.1:8001/menu/menus还有Bug，不能插入和取出时同时带有子健和子健别名
    """
    queryset = Menu.objects.filter(menu_type=1).all()
    serializer_class = MenuSerializer

    # def get_queryset(self):
    #     return Menu.objects.filter(menu_type=1).all()


class RightsViewSet(ListModelMixin,viewsets.GenericViewSet):
    """
    获取权限列表
    """
    queryset = Permission.objects.all()
    # serializer_class = PermissionSerializer2

    def get_serializer_class(self):
        # print(self.request.GET.get('type'))
        type = self.request.GET.get('type', None)
        if type=='list':

            return PermissionSerializer3
        else:
            return PermissionSerializer

    def get_queryset(self):
        type = self.request.GET.get('type', None)
        if type=='list':
            return Permission.objects.all()
        else:
            return Permission.objects.filter(level=1)