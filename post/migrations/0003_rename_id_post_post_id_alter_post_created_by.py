# Generated by Django 4.1.5 on 2023-02-01 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('post', '0002_alter_post_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='id',
            new_name='post_id',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='user.user'),
        ),
    ]
