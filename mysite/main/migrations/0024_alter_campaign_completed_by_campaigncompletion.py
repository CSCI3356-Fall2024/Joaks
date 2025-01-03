# Generated by Django 5.1.2 on 2024-11-28 03:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_merge_20241126_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='completed_by',
            field=models.ManyToManyField(blank=True, related_name='completed_by_campaigns', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CampaignCompletion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completion_date', models.DateTimeField(auto_now_add=True)),
                ('points_earned', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.campaign')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
