# Generated by Django 4.1.6 on 2023-05-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pubdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]