# Generated by Django 5.1.2 on 2024-10-22 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_customuser_finished_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='double_minor',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='minor',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]