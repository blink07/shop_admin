"""
Basic building blocks for generic class based views.

We don't bind behaviour to http method handlers yet,
which allows mixin classes to be composed in interesting ways.
"""
from __future__ import unicode_literals

# from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from .base import OK200
import pysnooper


def response_success(**kwargs):
    if kwargs.get("message", None):
        # return Response({"payload": kwargs["data"], "status": kwargs["status"], "message": kwargs["message"]})
        return Response({"payload": kwargs["data"], "status": OK200.status_code, "message": kwargs["message"]})
    else:
        return Response({"payload": kwargs["data"], "status": OK200.status_code})


def response_error(errmsg):
    return Response({"status": 0, "message": errmsg})


class CreateModelMixin:
    """
    Create a model instance.
    """
    @pysnooper.snoop()
    def create(self, request, *args, **kwargs):
        try:
            print(request.data)
            serializer = self.get_serializer(data=request.data)
            print("serializer:>>>>>>>>>>>>>>>>>>>>",serializer)
            serializer.is_valid(raise_exception=True)
            print(serializer)
            self.perform_create(serializer)
            # headers = self.get_success_headers(serializer.data)
            return response_success(data=serializer.data, message="提交成功")
        except Exception as e:
            return response_error(str(e))

    def perform_create(self, serializer):
        serializer.save()


class ListModelMixin:
    """
    List a queryset.
    """

    def list(self, request, *args, **kwargs):
        # try:
        queryset = self.filter_queryset(self.get_queryset())
        # print(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        # return Response(serializer.data)
        # print(serializer.data)
        return response_success(data=serializer.data)


        # except Exception as e:
        #     return response_error(str(e))


class RetrieveModelMixin:
    """
    Retrieve a model instance.
    """

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return response_success(data=serializer.data)
        except Exception as e:
            return response_error(str(e))


class UpdateModelMixin:
    """
    Update a model instance.
    """
    # @pysnooper.snoop
    def update(self, request,*args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}
            return response_success(data=serializer.data, message="更新成功")
        except Exception as e:
            return response_error(str(e))

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class DestroyModelMixin(object):
    """
    Destroy a model instance.
    """

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return response_success(data="",message="删除成功")
        except Exception as e:
            return response_error(str(e))

    def perform_destroy(self, instance):
        instance.delete()
