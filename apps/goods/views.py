from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters

from common.pagination import StandardResultsSetPagination
from goods.models import GoodsCategory
from goods.serializers import GoodsCategorySerializer, GoodsCategorySerializer2, GoodsCategorySerializer1
from utils.mixins import ListModelMixin, response_success


class CategoryList(ListModelMixin, viewsets.GenericViewSet):

    queryset = GoodsCategory.objects.all()
    serializer_class = GoodsCategorySerializer

    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('category_type', )

    def get_serializer_class(self):
        page = self.request.GET.get('pagenum', None)
        if page:
            return GoodsCategorySerializer
        else:
            return GoodsCategorySerializer1

    # def get_queryset(self):
    #     page = self.request.GET.get('pagenum', None)
    #     if page:
    #         return GoodsCategory.objects.all()
    #     else:
    #         return GoodsCategory.objects.filter(~Q(category_type=3))