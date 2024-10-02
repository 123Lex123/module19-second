from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


def main_page(request):
    posts = Post.objects.all().order_by('-created_at')

    # Получаем количество элементов на страницу из GET-запроса (по умолчанию 5)
    per_page = request.GET.get('per_page', 5)

    # Пагинация
    paginator = Paginator(posts, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {
        'page_obj': page_obj,
        'paginator': paginator,
        'per_page': per_page,  # Передаем значение количества элементов
    })
