# from rest_framework.views import exception_handler

import traceback
from django.core.exceptions import PermissionDenied
from rest_framework import status
# from rest_framework.compat import set_rollback
from rest_framework.response import Response
from rest_framework.exceptions import (AuthenticationFailed, MethodNotAllowed, NotAuthenticated,
                                       PermissionDenied as RestPermissionDenied,
                                       ValidationError,NotFound)
# from django.http import Http404, HttpResponseNotFound
# from django.shortcuts import get_object_or_404
# from component.constants import ResponseCodeStatus
# from common.log import logger
from rest_framework.views import set_rollback

from utils.error import ERROR_PermissionDenied, ERROR_ValidationError, ERROR_AuthenticationFailed


def exception_handler(exc, content):
    print("exc:",exc)
    data = {
        'result': False,
        'data': None
    }
    if isinstance(exc, (NotAuthenticated, AuthenticationFailed)):
        data = {
            'code': ERROR_AuthenticationFailed.status_code,
            'message': u'用户未登录或登录态失效，请使用登录链接重新登录'
            # 'login_url': ''  # 重定向到登录页
        }
        return Response(data, status=status.HTTP_403_FORBIDDEN)

    if isinstance(exc, PermissionDenied) or isinstance(exc, RestPermissionDenied):
        message = exc.detail if hasattr(exc, 'detail') else u'该用户没有该权限功能'
        data = {
            'code': ERROR_PermissionDenied.status_code,
            'message': message
        }
        return Response(data, status=status.HTTP_403_FORBIDDEN)

    else:
        if isinstance(exc, ValidationError):
            message = exc.detail if hasattr(exc, 'detail') else u'参数校验失败'
            data = {
                'code': ERROR_ValidationError.status_code,
                'message': message
            }

        elif isinstance(exc, MethodNotAllowed):
            message = exc.detail if hasattr(exc, 'detail') else u'请求方法不被允许'
            data = {
                'code': 400,
                'message': message
            }

        # elif isinstance(exc, Http404,HttpResponseNotFound):
        elif isinstance(exc, NotFound):
            # 这个好像捕捉不到，待考证
            print(404)
            # 更改返回的状态为为自定义错误类型的状态码
            data.update({
                'code': 500,
                'message': "aaa",
            })
        else:
            # 调试模式
            # logger.error(traceback.format_exc())
            # print traceback.format_exc()
            # if settings.RUN_MODE != 'PRODUCT':
            #     raise exc
            # 正式环境，屏蔽500
            data.update({
                'code': 500,
                'message': "服务器错误",
            })
            return Response(data, status=500)

        set_rollback()
        return Response(data, status=status.HTTP_200_OK)

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    # if response is not None:
    #     print(response.data)
    #     response.data.clear()
    #     response.data['code'] = response.status_code
    #     response.data['data'] = []
    #
    #     if response.status_code == 404:
    #         print(111)
    #         try:
    #             response.data['message'] = response.data.pop('detail')
    #             response.data['message'] = "Not found"
    #         except KeyError:
    #             response.data['message'] = "Not found"
    #
    #     if response.status_code == 400:
    #         response.data['message'] = 'Input error'
    #
    #     elif response.status_code == 401:
    #         response.data['message'] = "Auth failed"
    #
    #     elif response.status_code >= 500:
    #         response.data['message'] = "Internal service errors"
    #
    #     elif response.status_code == 403:
    #         response.data['message'] = "Access denied"
    #
    #     elif response.status_code == 405:
    #         response.data['message'] = 'Request method error'
    return response
