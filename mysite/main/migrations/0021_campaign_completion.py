# Generated by Django 5.1.2 on 2024-11-21 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_customuser_points_to_redeem_rewardredemption'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='completion',
            field=models.BooleanField(default=False),
        ),
    ]