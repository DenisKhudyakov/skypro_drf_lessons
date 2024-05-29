from rest_framework.pagination import PageNumberPagination


class LessonPaginator(PageNumberPagination):
    """Пагинатор уроков"""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CoursePaginator(PageNumberPagination):
    """Пагинатор курсов"""
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100