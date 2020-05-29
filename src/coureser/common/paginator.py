from django.core.paginator import Paginator


def paginate(objects_list, request, page_size=10):
    paginator = Paginator(objects_list, page_size)
    page = request.GET.get('page')
    objects_page = paginator.get_page(page)

    return objects_page, paginator
