# Generated by Django 5.1.2 on 2024-12-01 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_campaigncompletion_date_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='upcomingevents',
            name='unlimited',
            field=models.BooleanField(default=False),
        ),
    ]
