# Generated by Django 3.0.6 on 2020-06-04 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='time_minutes',
            field=models.IntegerField(default=0),
        ),
    ]
