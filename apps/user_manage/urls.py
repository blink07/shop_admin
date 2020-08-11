from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^testSentry$', views.TestSentry.as_view(),name="sentry测试"),
    url(r'^register/$', views.UserRegisterView.as_view({'post': 'create'}), name="自定义用户注册"),
    url(r'^userinfo/(?P<pk>\d+)$', views.UserRegisterView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name="用户详细信息"),
    url(r'^statechange/(?P<pk>\d+)/$', views.ChangeUserState.as_view(), name="改变用户状态"),

    # 角色模块
    url(r'^roleperlist/$', views.RolePermissionListView.as_view(), name="获取角色列表"),
    url(r'^roles/(?P<pk>\d+)/rights/(?P<pk1>\d+)$', views.RolePermissionListView.as_view(), name="删除角色的权限"),
    url(r'^(?P<pk>\d+)/rights/$', views.PermissionDistribution.as_view(), name="给角色添加权限"),

    url(r'roleList/$', views.RoleView.as_view({'get':'list'}), name="角色列表" ),

    url(r'changeRole/(?P<pk>\d+)/role/(?P<pk1>\d+)/$', views.ChangeUserRole.as_view(), name="更新用户角色")
]