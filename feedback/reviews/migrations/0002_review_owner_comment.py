# Generated by Django 3.2.9 on 2023-11-15 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='owner_comment',
            field=models.TextField(null=True),
        ),
    ]