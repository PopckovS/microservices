from django.contrib import admin
from blog.models import PostModel


class PostAdmin(admin.ModelAdmin):
    """Класс для кастомизации модели статей в админке"""
    pass


admin.site.register(PostModel, PostAdmin)

