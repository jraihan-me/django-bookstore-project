# Generated by Django 3.2.5 on 2021-07-08 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]