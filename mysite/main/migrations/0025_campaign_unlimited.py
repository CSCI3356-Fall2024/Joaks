# Generated by Django 5.1.2 on 2024-12-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_campaign_completed_by_campaigncompletion'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='unlimited',
            field=models.BooleanField(default=False),
        ),
    ]
