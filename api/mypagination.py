# This is the custom pagination for API
from rest_framework.pagination import LimitOffsetPagination
class MyLimitoffsetPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 15