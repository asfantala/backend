# Generated by Django 4.1.5 on 2023-08-21 09:42

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wanderHands', '0016_alter_image_image_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]