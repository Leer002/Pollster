# Generated by Django 4.2 on 2024-11-15 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_time',
            new_name='pub_date',
        ),
    ]