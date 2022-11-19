# Generated by Django 4.0.4 on 2022-10-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0030_subscriptionplan_highlight_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('highlight_status', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Picture'},
        ),
        migrations.CreateModel(
            name='PersonalPlanFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sub_plan', models.ManyToManyField(to='customer.personalplan')),
            ],
        ),
    ]