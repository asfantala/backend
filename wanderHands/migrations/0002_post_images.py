# Generated by Django 4.1.5 on 2023-08-06 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wanderHands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]