# Generated by Django 4.2.16 on 2024-11-04 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_customuser_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('locations', models.CharField(max_length=255)),
                ('show_news', models.BooleanField(default=True)),
                ('integration_method', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='events_images/')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='upcomingevents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
