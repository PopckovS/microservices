from django.db import models

"""
Модели для работы блога
"""


# class CategoryModel(models.Model):
#     pass

# class CommentaryModel(models.Model):
#     pass


class PostModel(models.Model):

    """Статья"""

    title = models.CharField(max_length=250, blank=False, null=False, verbose_name='Заголовок',
                             help_text='Заголовок для поста, обязательное поле, 250 символов максимум.')

    short_description = models.CharField(max_length=500, blank=True, null=True,
                                         verbose_name='Короткое описание',
                                         help_text='Короткое описание, не обязательное, 500 символов.')

    description = models.TextField(blank=False, null=False, verbose_name='Текст статьи',
                                   help_text='Текст статьи,  обязательное.')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        db_table = 'blog_post'

    def __str__(self):
        return self.title

