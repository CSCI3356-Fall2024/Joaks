# Generated by Django 5.1.2 on 2024-12-06 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_campaigncompletion_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='reward',
            name='locations',
            field=models.CharField(default='BEAN', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rewardredemption',
            name='location',
            field=models.CharField(choices=[('BEAN', 'The Bean Counter'), ('CARNEY', 'Carney Dining Room'), ('CAFE129', 'Café 129'), ('CHOC', 'Chocolate Bar'), ('CORO', 'CoRo Café & Market'), ('EAGLES', "Eagle's Nest"), ('HILLSIDE', 'Hillside Café'), ('LEGAL', 'Legal Grounds'), ('ADDIES', "The Loft @ Addie's"), ('LOWER', 'Lower Live'), ('LYONS', 'Lyons Hall'), ('STUART', 'Stuart Dining Hall'), ('BAKERY', 'BC Bakery'), ('CONCESSIONS', 'Concessions'), ('MARKET', 'The Market'), ('TULLY', 'Tully Cafe'), ('BROOK', 'Brookline Campus Dining Hall')], default='BEAN', max_length=255),
            preserve_default=False,
        ),
    ]