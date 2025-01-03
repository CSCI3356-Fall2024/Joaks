# Generated by Django 5.1.2 on 2024-11-22 18:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_campaign_completion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='completion',
        ),
        migrations.AddField(
            model_name='campaign',
            name='completed_by',
            field=models.ManyToManyField(blank=True, related_name='completed_campaigns', to=settings.AUTH_USER_MODEL),
        ),
    ]
