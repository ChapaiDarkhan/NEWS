# Generated by Django 3.1.4 on 2021-01-25 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20210125_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='time',
            new_name='created_at',
        ),
    ]