# Generated by Django 4.2.16 on 2024-11-05 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_customuser_is_first_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('show_news', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='milestones_images/')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='milestones', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
