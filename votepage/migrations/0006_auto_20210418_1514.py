# Generated by Django 3.1.6 on 2021-04-18 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votepage', '0005_feedback_updates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='response',
            new_name='feedback',
        ),
    ]
