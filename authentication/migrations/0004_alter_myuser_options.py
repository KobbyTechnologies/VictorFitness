# Generated by Django 4.0.3 on 2022-04-01 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_myuser_is_email_verified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name_plural': 'Add User'},
        ),
    ]
