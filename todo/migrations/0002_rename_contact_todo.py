# Generated by Django 4.1.2 on 2022-10-18 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Todo',
        ),
    ]
