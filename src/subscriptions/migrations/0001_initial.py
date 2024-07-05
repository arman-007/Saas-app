# Generated by Django 5.0.6 on 2024-07-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'permissions': [('basic', 'Basic Perm'), ('pro', 'Pro Perm'), ('advanced', 'Advance Perm')],
            },
        ),
    ]