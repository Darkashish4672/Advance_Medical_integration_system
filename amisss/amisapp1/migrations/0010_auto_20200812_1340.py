# Generated by Django 2.2.12 on 2020-08-12 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amisapp1', '0009_usertype_table_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientbookappointment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='patientbookappointment',
            name='massage',
        ),
        migrations.AddField(
            model_name='usertype_table',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
