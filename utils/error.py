# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import base


class SUCCESS(base.OK200):
    message = u"操作成功~~"


class ERROR_FAULT(base.ServiceUnavailable503):
    message = u"服务器内部错误~~"


class ERROR_COMMON(base.InternalServerError500):
    message = u'未知异常~~'


class CODE_ERROR_COMMON(base.CodeError555):
    message = u'未知异常~~'


class ERROR_USER_RALATION(base.UserOrPasswordError):
    message = u'用户名或密码错误~~'


class ERROR_SOCKET(base.UserOrPasswordError):
    message = u'socket通讯异常~~'

class ERROR_AuthenticationFailed(base.Unauthorized401):
    message = u'用户未登录或登录态失效，请使用登录链接重新登录'

class ERROR_PermissionDenied(base.PermissionDenied406):
    message = u'该用户没有该权限功能'

class ERROR_ValidationError(base.ValidationError512):
    message = u'参数校验失败'

class ERROR_NotFound(base.NotFound404):
    message = u'请求接口为找到'

class ERROR_MethodNotAllowed(base.MethodNotAllowed405):
    message = u'该请求未被允许'