# Generated by Django 3.2.7 on 2021-10-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdl', '0021_auto_20211011_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]