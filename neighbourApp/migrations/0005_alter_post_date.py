# Generated by Django 4.0.4 on 2022-04-19 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourApp', '0004_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(),
        ),
    ]