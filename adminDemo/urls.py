"""adminDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework_jwt.views import obtain_jwt_token

import goods.urls
from user_manage.views import GetCodeInfo, UserList, CustomResponseObtainJSONWebToken
# from rest_framework.authtoken import views
# from user_manage import urls
# from menu import urls
import user_manage.urls
import menu.urls

from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="Shop API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.blink07.com/policies/terms/",
      contact=openapi.Contact(email="2954538230@qq.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # swagger接口文档路由
    url(r'^docs/', schema_view, name="docs"),
    url(r'getcodeinfo/$', GetCodeInfo.as_view()),
    # url(r'login/', views.obtain_auth_token),
    # path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/', UserList.as_view({'get': 'list'})),
    url(r'user/', include(user_manage.urls)),
    # jwt的认证接口, 自定义登录
    path('login/', CustomResponseObtainJSONWebToken.as_view()),  # 写重写jwt认证类
    url(r'menu/', include(menu.urls)),
    url(r'goods/', include(goods.urls)),

    # swagger
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('chat/', include('dashboard.urls')),

] + static(settings.STATIC_URL, serve, document_root = settings.STATIC_ROOT)

# handler404 = Response(data={}, status=status.HTTP_404_NOT_FOUND,)
# urlpatterns += [
#
# ]