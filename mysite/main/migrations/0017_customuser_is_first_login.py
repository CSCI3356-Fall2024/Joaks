# Generated by Django 5.1.2 on 2024-11-04 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_customuser_is_first_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_first_login',
            field=models.BooleanField(default=True),
        ),
    ]
