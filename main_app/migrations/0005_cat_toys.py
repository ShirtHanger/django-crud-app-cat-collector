# Generated by Django 5.1.3 on 2024-12-07 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_toy'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]
