# Generated by Django 4.0.3 on 2022-03-30 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_remove_topic_video_topic_videofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programattachments',
            name='file',
        ),
        migrations.AddField(
            model_name='programattachments',
            name='filepath',
            field=models.FileField(null=True, upload_to='files/', verbose_name=''),
        ),
    ]
