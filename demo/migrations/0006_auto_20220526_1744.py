# Generated by Django 2.2.2 on 2022-05-26 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_auto_20220526_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textpost',
            name='image_content',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
