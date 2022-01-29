from django.db import models
from django.urls import reverse

"""
Модели для работы блога
"""


class CommentaryModel(models.Model):
    """Комментарии для постов"""

    text = models.CharField(max_length=500, blank=False, null=False, verbose_name='Текст комментария')

    # Каждый комментарий связан с постом, отношение 1:M
    parent_post = models.ForeignKey('PostModel', blank=False, null=True,
                                    verbose_name='Пост', on_delete=models.CASCADE)

    class Meta:
        db_table = 'blog_commentary'
        verbose_name = 'Комментарий для поста'
        verbose_name_plural = 'Комментарии для постов'

    def __str__(self):
        return self.pk


class CategoryModel(models.Model):
    """Категория для постов пользователей"""

    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Название категории',
                            help_text='Название категории, обязательное, 100 символов.')

    class Meta:
        db_table = 'blog_category'
        verbose_name = 'Категория статьи'
        verbose_name_plural = 'Категория статей'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Возвращает абсолютный путь к конкретному объекту модели по ее pk"""
        return reverse('blog_one_category', kwargs={'category_id': self.pk})


class PostModel(models.Model):
    """Посты пользователей, связаны с категориями и тегами"""

    title = models.CharField(max_length=250, blank=False, null=False, verbose_name='Заголовок',
                             help_text='Заголовок для поста, обязательное поле, 250 символов максимум.')

    short_description = models.CharField(max_length=500, blank=True, null=True,
                                         verbose_name='Короткое описание',
                                         help_text='Короткое описание, не обязательное, 500 символов.')

    description = models.TextField(blank=False, null=False, verbose_name='Текст статьи',
                                   help_text='Текст статьи,  обязательное.')

    create_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')

    update_date = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')

    publish = models.BooleanField(default=True, verbose_name='Публиковать да/нет ?')

    # Каждый пост связан с привязан к категории, отношение 1:M
    parent_category = models.ForeignKey('CategoryModel', blank=False, null=True,
                                        verbose_name='Категория статьи', on_delete=models.PROTECT)

    # post_tags = models.ManyToManyField('TagsModel', through='PostTagsModel')
    post_tags = models.ManyToManyField('TagsModel', blank=True)

    class Meta:
        db_table = 'blog_post'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Возвращает абсолютный путь к конкретному объекту модели по ее pk"""
        return reverse('blog_one_post', kwargs={'post_id': self.pk})


# class PostTagsModel(models.Model):
#     """Связующая модель между TagsModel и PostModel связью M:M"""
#     tagsmodel_id = models.ForeignKey('TagsModel', blank=False, null=True,
#                                      on_delete=models.CASCADE)
#     postmodel_id = models.ForeignKey('PostModel', blank=False, null=True,
#                                      on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'blog_post_post_tag'


class TagsModel(models.Model):
    """Теги для постов, связаны с постами связью M:M"""
    name = models.CharField(max_length=50, blank=False, null=False,
                            verbose_name='Название тега')

    class Meta:
        db_table = 'blog_tags'
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
