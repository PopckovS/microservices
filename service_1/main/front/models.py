from django.db import models


class NewsModel(models.Model):
    id = models.AutoField(verbose_name='Новость', primary_key=True)
    title = models.CharField(verbose_name='Заголовок', max_length=255, blank=True)
    content = models.TextField(verbose_name='Текст', blank=True)
    category_id = models.ForeignKey("CategoryModel", on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        db_table = 'main_news'


class CategoryModel(models.Model):
    id = models.AutoField(verbose_name='Категория', primary_key=True)
    title = models.CharField(verbose_name='Заголовок', max_length=255, blank=True)
    content = models.TextField(verbose_name='Текст', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'main_category'


