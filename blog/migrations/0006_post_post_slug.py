# Generated by Django 3.0.6 on 2020-05-31 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
