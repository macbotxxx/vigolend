# Generated by Django 3.1.11 on 2021-06-01 11:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210601_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique identifier of the customer.', primary_key=True, serialize=False),
        ),
    ]