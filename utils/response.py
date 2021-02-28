from rest_framework.response import Response

from utils.error import SUCCESS


def response(data=None, error=SUCCESS, **kwargs):

    return Response(data={"payload":data, "message":error.message, "code":error.status_code})
