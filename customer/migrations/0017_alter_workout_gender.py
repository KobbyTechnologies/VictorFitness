# Generated by Django 4.0.4 on 2022-05-01 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0016_alter_workout_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.userinfo'),
        ),
    ]
