# Generated by Django 4.1.6 on 2023-05-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_alter_article_comparison_alter_article_imageurl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='imageurl',
            field=models.URLField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(blank=True, max_length=50000),
        ),
    ]
