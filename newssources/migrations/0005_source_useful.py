# Generated by Django 4.1.7 on 2023-05-17 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newssources', '0004_alter_source_author_alter_source_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='useful',
            field=models.BooleanField(default=True),
        ),
    ]
