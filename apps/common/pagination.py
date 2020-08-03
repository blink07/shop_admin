from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination

from utils.mixins import response_success


class StandardResultsSetPagination(PageNumberPagination):
    # page_size = 1
    """
    自定义分页，
    """
    page_size_query_param = 'pagesize'  # 自定义查询的结果的每一页大小参数
    page_query_param = 'pagenum'  # 自定义查询第几页参数
    max_page_size = 1000 # 自定义查询最多多少页

    def get_paginated_response(self, data):
        """
        自定义返回结果格式
        :param data:
        :return:
        """
        return response_success(data=OrderedDict([
            ('total', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))