# Generated by Django 5.0.4 on 2024-04-15 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_category_remove_books_category_books_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.ManyToManyField(null=True, to='market.category', verbose_name='Category'),
        ),
    ]
