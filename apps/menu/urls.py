from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^menus$', MenuViewSet.as_view({'get':'list', 'post':'create'}),name="获取左侧菜单导航栏"),
    # url(r'^rights/list$', RightsViewSet.as_view({'get':'list'}),name="获取权限列表"),
    url(r'^rights$', RightsViewSet.as_view({'get':'list'}),name="获取权限列表"),

]