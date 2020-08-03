# -*- coding: utf-8 -*-
from abc import ABCMeta


class BaseReturn(Exception):
    __metaclass__ = ABCMeta


# 1XX Informational
class Continue100(BaseReturn):
    status_code = 100


class SwitchingProtocols101(BaseReturn):
    status_code = 101


class Processing102(BaseReturn):
    status_code = 102


# 2XX Success
class OK200(BaseReturn):
    status_code = 200


class Created201(BaseReturn):
    status_code = 201


# 4XX Client Error
class BadRequest400(BaseReturn):
    status_code = 400


class Unauthorized401(BaseReturn):
    status_code = 401


class PaymentRequired402(BaseReturn):
    status_code = 402


class Forbidden403(BaseReturn):
    status_code = 403


class NotFound404(BaseReturn):
    status_code = 404


class MethodNotAllowed405(BaseReturn):
    status_code = 405

class PermissionDenied406(BaseReturn):
    status_code = 406

class RequestTimeout408(BaseReturn):
    status_code = 408

# 5XX Server Error

class InternalServerError500(BaseReturn):
    status_code = 500

class CodeError555(BaseReturn):
    status_code = 555

class NotImplemented501(BaseReturn):
    status_code = 501


class BadGateway502(BaseReturn):
    status_code = 502


class ServiceUnavailable503(BaseReturn):
    status_code = 503


class GatewayTimeout504(BaseReturn):
    status_code = 504


class HTTPVersionNotSupported505(BaseReturn):
    status_code = 505


class VariantAlsoNegotiates506(BaseReturn):
    status_code = 506


class InsufficientStorage507(BaseReturn):
    status_code = 507


class LoopDetected508(BaseReturn):
    status_code = 508


class NotExtended510(BaseReturn):
    status_code = 510


class NetworkAuthenticationRequired511(BaseReturn):
    status_code = 511


class NetworkConnectTimeoutError599(BaseReturn):
    status_code = 599


class SocketProcessError520(BaseReturn):
    status_code = 520

class ValidationError512(BaseReturn):
    status_code = 521

class UserOrPasswordError(BaseReturn):
    status_code=600


