# Generated by Django 3.2.7 on 2021-10-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdl', '0011_auto_20211004_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='latitude',
            field=models.FloatField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='longitude',
            field=models.FloatField(blank=True, max_length=40, null=True),
        ),
    ]
