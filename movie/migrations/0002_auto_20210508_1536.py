# Generated by Django 3.1.3 on 2021-05-08 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='current',
            name='current_poster',
            field=models.TextField(),
        ),
    ]
