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

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)
        page = self.paginate_queryset(queryset)
        print("page>>>>>>>>>>",page)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)
        print(serializer.data)
        return response_success(data=serializer.data)

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