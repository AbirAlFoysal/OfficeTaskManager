# Generated by Django 4.1.7 on 2023-06-02 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0021_alter_profile_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('media', models.FileField(blank=True, null=True, upload_to='chat_media')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='m_receiver', to='users.profile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='m_sender', to='users.profile')),
            ],
        ),
    ]
