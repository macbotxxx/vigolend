# Generated by Django 3.1.11 on 2021-06-01 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_useraddress_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='city',
            field=models.CharField(blank=True, help_text='The city of the address of the user.', max_length=50, null=True, verbose_name='City'),
        ),
    ]
