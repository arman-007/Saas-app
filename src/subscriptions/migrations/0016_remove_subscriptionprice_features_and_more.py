# Generated by Django 5.0.6 on 2024-07-13 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0015_subscriptionprice_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptionprice',
            name='features',
        ),
        migrations.AddField(
            model_name='subscription',
            name='features',
            field=models.TextField(blank=True, help_text='features for pricing, separated by new line', null=True),
        ),
    ]
