# Необходимо выполнять в django-shell
from .models import Article


# Создание объектов
Article.objects.create(title='First Article', content='Content of the first article', author='Author1')
Article.objects.create(title='Second Article', content='Content of the second article', author='Author2')

# Изменение заголовка статьи
article = Article.objects.get(id=1)
article.title = 'Updated First Article'
article.save()

# Получение всех объектов
all_articles = Article.objects.all()
for article in all_articles:
    print(article.title, article.content)

# Удаление статьи
article_to_delete = Article.objects.get(id=2)
article_to_delete.delete()

# Фильтрация по автору
admin_articles = Article.objects.filter(author='Author1')
for article in admin_articles:
    print(article.title)
