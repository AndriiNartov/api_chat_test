from django.core.paginator import Paginator

from .models import Message


def make_custom_paginated_queryset(page_number, paginate_by):
    '''
    According to test task we need to implement pagination, but instead of query params
    user should type page_number in URL path (e.g. /api/messages/list/0). For this purpose was created the function.
    In the first row of the function we increase page_number by 1, because according to test task
    we can receive this argument with value 0, but our pages numbers should start with value 1.
    '''

    page_number += 1
    queryset_to_paginate = Message.objects.all()
    paginator = Paginator(queryset_to_paginate, paginate_by)
    queryset = paginator.get_page(page_number)
    return queryset
