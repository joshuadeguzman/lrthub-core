# Generated by Django 2.0.7 on 2018-07-14 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_auto_20180714_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='ad_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
