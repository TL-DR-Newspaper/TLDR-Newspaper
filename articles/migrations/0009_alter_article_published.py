# Generated by Django 4.1.7 on 2023-05-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_article_created_by_ai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
