# from django.http import JsonResponse
# from django.utils.deprecation import MiddlewareMixin
# from django.core.exceptions import PermissionDenied
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.exceptions import (AuthenticationFailed, MethodNotAllowed, NotAuthenticated,
#                                        PermissionDenied as RestPermissionDenied,
#                                        ValidationError,NotFound)
# from rest_framework.views import set_rollback
#
# from utils.error import ERROR_PermissionDenied, ERROR_ValidationError, ERROR_AuthenticationFailed
#
#
# class ExceptionMiddleware(MiddlewareMixin):
#
#     def process_view(self, request, _, view_args, view_kwargs):
#         pass
#
#     def process_exception(self, request, exc):
#
#         print("exc:", exc)
#         data = {
#             'result': False,
#             'data': None
#         }
#         if isinstance(exc, (NotAuthenticated, AuthenticationFailed)):
#             data = {
#                 'code': ERROR_AuthenticationFailed.status_code,
#                 'message': u'用户未登录或登录态失效，请使用登录链接重新登录'
#                 # 'login_url': ''  # 重定向到登录页
#             }
#             return Response(data, status=status.HTTP_403_FORBIDDEN)
#
#         if isinstance(exc, PermissionDenied) or isinstance(exc, RestPermissionDenied):
#             message = exc.detail if hasattr(exc, 'detail') else u'该用户没有该权限功能'
#             data = {
#                 'code': ERROR_PermissionDenied.status_code,
#                 'message': message
#             }
#             return Response(data, status=status.HTTP_403_FORBIDDEN)
#
#         else:
#             if isinstance(exc, ValidationError):
#                 message = exc.detail if hasattr(exc, 'detail') else u'参数校验失败'
#                 data = {
#                     'code': ERROR_ValidationError.status_code,
#                     'message': message
#                 }
#
#             elif isinstance(exc, MethodNotAllowed):
#                 message = exc.detail if hasattr(exc, 'detail') else u'请求方法不被允许'
#                 data = {
#                     'code': 400,
#                     'message': message
#                 }
#
#             # elif isinstance(exc, Http404,HttpResponseNotFound):
#             elif isinstance(exc, NotFound):
#                 # 这个好像捕捉不到，待考证
#                 print(404)
#                 # 更改返回的状态为为自定义错误类型的状态码
#                 data.update({
#                     'code': 500,
#                     'message': "aaa",
#                 })
#             else:
#                 # 调试模式
#                 # logger.error(traceback.format_exc())
#                 # print traceback.format_exc()
#                 # if settings.RUN_MODE != 'PRODUCT':
#                 #     raise exc
#                 # 正式环境，屏蔽500
#                 print("@@@@@@@@@", exc)
#                 data.update({
#                     'code': 500,
#                     'message': "服务器错误",
#                 })
#                 print(data)
#                 return JsonResponse(data, status=500)
#
#             # set_rollback()
#             return Response(data, status=status.HTTP_200_OK)