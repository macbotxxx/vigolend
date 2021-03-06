# Generated by Django 3.1.11 on 2021-06-01 23:16

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique identifier of an object.', primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Timestamp when the record was created.', max_length=20, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Modified date when the record was created.', max_length=20, verbose_name='Modified Date')),
                ('name', models.CharField(blank=True, help_text='Team member full name', max_length=50, null=True, verbose_name='Team Member name')),
                ('designation', models.CharField(blank=True, help_text='The position of the team member.', max_length=50, null=True, verbose_name='Designation')),
                ('facebook', models.CharField(blank=True, help_text='The facebook link of the team member.', max_length=50, null=True, verbose_name='Facebook link')),
                ('twitter', models.CharField(blank=True, help_text='The twitter handle- without `@`.', max_length=50, null=True, verbose_name='Twitter Handle')),
                ('photo', models.ImageField(blank=True, help_text='Photo of the team member.', null=True, upload_to='images', verbose_name='Profile Image')),
            ],
            options={
                'verbose_name': 'Team Member',
                'verbose_name_plural': 'Team Member',
            },
        ),
    ]
