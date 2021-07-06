from rest_framework.pagination import LimitOffsetPagination


class SmallSetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class MediumSetPagination(LimitOffsetPagination):
    default_limit = 50
    max_limit = 500


class LargeSetPagination(LimitOffsetPagination):
    default_limit = 100
    max_limit = 1000
