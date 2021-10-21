# Generated by Django 3.2.7 on 2021-10-20 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdl', '0031_alter_menuitem_dietary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='day',
            field=models.CharField(blank=True, choices=[('all_days', 'ALL DAYS'), ('weekdays', 'Weekdays'), ('weekends', 'Weekends'), ('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], default='ALL DAYS', max_length=40, null=True),
        ),
    ]
