# Generated by Django 2.2 on 2019-05-19 07:03

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('third_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='userprofileinfo',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
