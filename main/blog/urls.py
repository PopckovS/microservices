from django.urls import path
from blog import views

# для использования в шаблонах, для создания ссылки
# app_name = 'blog'


urlpatterns = [
    # путь для главной странице
    path('', views.index, name='blog_home'),

    # пути для категорий
    path('category/', views.show_all_category, name='blog_all_category'),
    path('category/<int:category_id>/', views.show_one_category, name='blog_one_category'),

    # пути для статей
    path('post/', views.show_all_post, name='blog_all_post'),
    path('post/<int:post_id>/', views.show_one_post, name='blog_one_post'),
]
