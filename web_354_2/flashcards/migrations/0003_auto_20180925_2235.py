# Generated by Django 2.1.1 on 2018-09-25 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0002_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='firest_name',
            new_name='first_name',
        ),
    ]
