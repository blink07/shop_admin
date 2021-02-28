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

from utils.error import ERROR_PermissionDenied, ERROR_ValidationError, ERROR_AuthenticationFailed, ERROR_FAULT, \
    ERROR_NotFound, SUCCESS, ERROR_MethodNotAllowed
from utils.response import response


def exception_handler(exc, content):
    error = SUCCESS
    if isinstance(exc, (NotAuthenticated, AuthenticationFailed)):
        # data = {
        #     'code': ERROR_AuthenticationFailed.status_code,
        #     'message': u'用户未登录或登录态失效，请使用登录链接重新登录'
        #     # 'login_url': ''  # 重定向到登录页
        # }
        # return Response(data, status=status.HTTP_403_FORBIDDEN)
        error = ERROR_AuthenticationFailed

    if isinstance(exc, PermissionDenied) or isinstance(exc, RestPermissionDenied):
        # message = exc.detail if hasattr(exc, 'detail') else u'该用户没有该权限功能'
        # data = {
        #     'code': ERROR_PermissionDenied.status_code,
        #     'message': message
        # }
        error = ERROR_PermissionDenied
        error.message = exc.detail if hasattr(exc, 'detail') else u'该用户没有该权限功能'
        # return Response(data, status=status.HTTP_403_FORBIDDEN)

    else:
        if isinstance(exc, ValidationError):
            # message = exc.detail if hasattr(exc, 'detail') else u'参数校验失败'
            # data = {
            #     'code': ERROR_ValidationError.status_code,
            #     'message': message
            # }
            error = ERROR_ValidationError
            error.message = exc.detail if hasattr(exc, 'detail') else u'参数校验失败'

        elif isinstance(exc, MethodNotAllowed):
            # message = exc.detail if hasattr(exc, 'detail') else u'请求方法不被允许'
            # data = {
            #     'code': 400,
            #     'message': message
            # }
            error = ERROR_MethodNotAllowed
            error.message = exc.detail if hasattr(exc, 'detail') else u'请求方法不被允许'
        # elif isinstance(exc, Http404,HttpResponseNotFound):
        elif isinstance(exc, NotFound):
            # 这个好像捕捉不到，待考证
            # print(404)
            # # 更改返回的状态为为自定义错误类型的状态码
            # return response(error=ERROR_NotFound)
            error = ERROR_NotFound
        else:
            # 调试模式
            # logger.error(traceback.format_exc())
            # print traceback.format_exc()
            # if settings.RUN_MODE != 'PRODUCT':
            #     raise exc
            # 正式环境，屏蔽500
            # data.update({
            #     'code': 500,
            #     'message': "服务器错误",
            # })
            # return Response(data, status=500)
            error = ERROR_FAULT
            # return response(error=ERROR_FAULT)

        set_rollback()
        # return Response(data, status=status.HTTP_200_OK)
        return response(error=error)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    return response
