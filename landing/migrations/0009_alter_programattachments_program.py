# Generated by Django 4.0.3 on 2022-03-30 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_alter_programattachments_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programattachments',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='landing.program_detail'),
        ),
    ]