# Generated by Django 2.1.7 on 2019-06-02 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20190602_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='dob',
        ),
    ]
