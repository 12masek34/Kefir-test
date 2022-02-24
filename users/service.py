from rest_framework.pagination import PageNumberPagination


class PaginationUsers(PageNumberPagination):
    page_size = 3
    max_page_size = 1000


def set_data_and_meta(serializer, meta):
    list_data = []
    list_meta = []
    for i in serializer.data:
        list_data.append(i)
    for i in meta.data:
        list_meta.append(i)
    res = list(zip(list_data, list_meta))
    return res
