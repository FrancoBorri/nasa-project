# Generated by Django 5.1.6 on 2025-02-20 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asteroids', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracked_asteroid',
            old_name='asteroid_id',
            new_name='asteroid',
        ),
        migrations.RenameField(
            model_name='tracked_asteroid',
            old_name='user_id',
            new_name='user',
        ),
    ]
