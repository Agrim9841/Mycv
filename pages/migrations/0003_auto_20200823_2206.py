# Generated by Django 3.1 on 2020-08-23 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200823_2042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='full_name',
            new_name='name',
        ),
    ]
