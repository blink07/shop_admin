from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'categoryList', CategoryList.as_view({'get':'list'}))
]