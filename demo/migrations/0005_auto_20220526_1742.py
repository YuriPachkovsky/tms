# Generated by Django 2.2.2 on 2022-05-26 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20220526_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textpost',
            name='image_content',
            field=models.ImageField(blank=True, null=True, upload_to='media/images'),
        ),
    ]