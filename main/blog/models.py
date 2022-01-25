from django.db import models

"""
Модели для работы блога
"""


# class CommentaryModel(models.Model):
#     pass


class CategoryModel(models.Model):
    """Категория для статей"""

    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Название категории',
                            help_text='Название категории, обязательное, 100 символов.')

    class Meta:
        verbose_name = 'Категория статьи'
        verbose_name_plural = 'Категория статей'
        db_table = 'blog_category'

    def __str__(self):
        return self.name


class PostModel(models.Model):
    """Статья"""

    title = models.CharField(max_length=250, blank=False, null=False, verbose_name='Заголовок',
                             help_text='Заголовок для поста, обязательное поле, 250 символов максимум.')

    short_description = models.CharField(max_length=500, blank=True, null=True,
                                         verbose_name='Короткое описание',
                                         help_text='Короткое описание, не обязательное, 500 символов.')

    description = models.TextField(blank=False, null=False, verbose_name='Текст статьи',
                                   help_text='Текст статьи,  обязательное.')

    parent_category = models.ForeignKey('CategoryModel', blank=False, null=False,
                                        verbose_name='Категория статьи', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        db_table = 'blog_post'

    def __str__(self):
        return self.title

