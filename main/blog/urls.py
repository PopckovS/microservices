from django.urls import path
from blog import views

# для использования в шаблонах, для создания ссылки
app_name = 'blog'


urlpatterns = [
    path('', views.index, name='blog_home'),
    path('category/<int:category_id>/', views.show_category, name='blog_category'),
]
