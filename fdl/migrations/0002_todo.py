# Generated by Django 3.2.7 on 2021-09-22 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
