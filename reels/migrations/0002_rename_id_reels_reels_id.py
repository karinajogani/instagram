# Generated by Django 4.1.5 on 2023-02-01 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reels', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reels',
            old_name='id',
            new_name='reels_id',
        ),
    ]
