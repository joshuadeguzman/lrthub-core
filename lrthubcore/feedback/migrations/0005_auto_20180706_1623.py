# Generated by Django 2.0.7 on 2018-07-06 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20180706_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackconversation',
            name='address',
            field=models.CharField(max_length=255),
        ),
    ]