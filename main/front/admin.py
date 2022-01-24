from django.contrib import admin

from .models import CategoryModel, NewsModel


class CategoryAdmin(admin.ModelAdmin):
    pass


class NewsAdmin(admin.ModelAdmin):
    pass


admin.site.register(CategoryModel)
admin.site.register(NewsModel)

