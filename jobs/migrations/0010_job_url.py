# Generated by Django 3.0.5 on 2020-04-06 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_position_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='url',
            field=models.URLField(default=''),
        ),
    ]