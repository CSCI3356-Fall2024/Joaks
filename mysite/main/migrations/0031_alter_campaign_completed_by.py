# Generated by Django 5.1.2 on 2024-12-03 00:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_merge_20241202_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='completed_by',
            field=models.ManyToManyField(blank=True, related_name='completed_by_campaigns', to=settings.AUTH_USER_MODEL),
        ),
    ]
