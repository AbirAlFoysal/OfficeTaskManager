# Generated by Django 4.1.2 on 2023-01-31 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_remove_profile_is_varified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email_token',
        ),
    ]
