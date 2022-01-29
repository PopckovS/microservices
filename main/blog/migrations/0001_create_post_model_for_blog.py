# Generated by Django 3.2.10 on 2022-01-25 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Заголовок для поста, обязательное поле, 250 символов максимум.', max_length=250, verbose_name='Заголовок')),
                ('short_description', models.CharField(blank=True, help_text='Короткое описание, не обязательное, 500 символов.', max_length=500, null=True, verbose_name='Короткое описание')),
                ('description', models.TextField(help_text='Текст статьи,  обязательное.', verbose_name='Текст статьи')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'db_table': 'blog_post',
            },
        ),
    ]