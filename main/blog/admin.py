from django.contrib import admin
from blog.models import PostModel, CategoryModel, CommentaryModel, TagsModel


class PostAdmin(admin.ModelAdmin):
    """Класс для кастомизации модели статей в админке"""
    pass


class CategoryAdmin(admin.ModelAdmin):
    """Класс для кастомизации модели категорий статей в админке"""
    pass


admin.site.register(PostModel, PostAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(CommentaryModel)
admin.site.register(TagsModel)
