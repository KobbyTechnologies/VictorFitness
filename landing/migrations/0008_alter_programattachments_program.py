# Generated by Django 4.0.3 on 2022-03-30 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_alter_programattachments_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programattachments',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='landing.topic'),
        ),
    ]
