# Generated by Django 4.1.7 on 2023-03-31 15:12

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskManager', '0007_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='taskManager.project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='link',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, default='No description provided', null=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, default='No description provided', null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(default='No description provided'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='commentOnCompletion',
            field=ckeditor.fields.RichTextField(blank=True, default='No comments', null=True),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, default='No description provided', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, default='No description provided', null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
