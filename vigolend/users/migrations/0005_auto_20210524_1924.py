# Generated by Django 3.1.11 on 2021-05-24 17:24

from django.db import migrations
import vigolend.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210524_1911'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', vigolend.users.models.UserManager()),
            ],
        ),
    ]