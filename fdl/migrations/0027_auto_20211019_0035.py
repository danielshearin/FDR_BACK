# Generated by Django 3.2.7 on 2021-10-19 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdl', '0026_alter_menuitem_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='day',
            field=models.CharField(blank=True, choices=[('all_days', 'ALL DAYS'), ('weekends', 'Weekends'), ('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], default='ALL DAYS', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='dietary',
            field=models.CharField(blank=True, choices=[('none', 'none'), ('vegan', 'Vegan'), ('vegetarian', 'Vegetarian'), ('gluten_free', 'Gluten-Free'), ('vegetarian_and_gf', 'Vegetarian and GF'), ('vegan_and_gf', 'Vegan and GF')], default='none', max_length=40, null=True),
        ),
    ]
