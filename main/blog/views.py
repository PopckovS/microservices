from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import PostModel, CategoryModel


def get_main_menu():
    return [
        # {'title': 'Админка', 'url_name': 'admin'},
        {'title': 'Главная страница', 'url_name': 'blog_home'},
        {'title': 'Все категории', 'url_name': 'blog_all_category'},
        {'title': 'Все статьи', 'url_name': 'blog_all_post'},
    ]


def index(request):
    """Главная страница блога"""
    context = {
        'title': 'Главная страница Блога',
        'menu': get_main_menu(),
    }
    return render(request, 'blog/index.html', context=context)


def show_all_category(request):
    """Показывает все категории что есть"""
    all_category = CategoryModel.objects.all()
    context = {
        'title': 'Все категории',
        'menu': get_main_menu(),
        'all_category': all_category
    }
    return render(request, 'blog/categories.html', context=context)


def show_one_category(request, category_id):
    """Показать все статьи одной категории"""
    posts = PostModel.objects.filter(parent_category=category_id)
    context = {
        'title': 'Одна категория',
        'menu': get_main_menu(),
        'posts': posts,
    }
    return render(request, 'blog/category.html', context=context)


def show_all_post(request):
    """Показать все статьи"""
    posts = PostModel.objects.all()
    context = {
        'title': 'Все статьи что есть',
        'menu': get_main_menu(),
        'posts': posts,
    }
    return render(request, 'blog/posts.html', context=context)


def show_one_post(request, post_id):
    """Показать одну конкретную статью"""
    post = PostModel.objects.get(pk=post_id)
    context = {
        'title': 'Одна статья',
        'menu': get_main_menu(),
        'post': post,
    }
    return render(request, 'blog/post.html', context=context)
