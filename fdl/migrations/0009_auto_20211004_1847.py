# Generated by Django 3.2.7 on 2021-10-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdl', '0008_alter_menuitem_dietary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='item',
            field=models.CharField(max_length=100),
        ),
    ]
