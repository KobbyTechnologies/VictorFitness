# Generated by Django 4.0.3 on 2022-04-21 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0002_userinfo_delete_user_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='names',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]