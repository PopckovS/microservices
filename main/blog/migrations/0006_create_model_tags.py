# Generated by Django 3.2.10 on 2022-01-29 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_create_model_commentary'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'db_table': 'blog_tags',
            },
        ),
    ]
