# Generated by Django 4.1.2 on 2022-12-16 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
