# Generated by Django 4.1.7 on 2023-04-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0009_subtask_created_by_subtask_related_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
