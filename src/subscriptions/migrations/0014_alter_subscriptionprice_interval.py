# Generated by Django 5.0.6 on 2024-07-13 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0013_alter_subscriptionprice_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionprice',
            name='interval',
            field=models.CharField(choices=[('month', 'MONTHLY'), ('year', 'Yearly')], default='month', max_length=120),
        ),
    ]