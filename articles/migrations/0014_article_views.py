# Generated by Django 4.1.6 on 2023-05-19 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_article_long_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]