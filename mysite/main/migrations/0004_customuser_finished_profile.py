# Generated by Django 5.1.2 on 2024-10-22 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_customuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='finished_profile',
            field=models.BooleanField(default=False),
        ),
    ]
