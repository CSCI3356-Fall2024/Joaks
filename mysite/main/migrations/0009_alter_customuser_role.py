# Generated by Django 5.1.2 on 2024-11-04 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_campaign_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Student', 'Student'), ('Supervisor', 'Supervisor')], default='Student', max_length=20),
        ),
    ]
