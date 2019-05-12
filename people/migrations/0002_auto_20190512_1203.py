# Generated by Django 2.1.7 on 2019-05-12 12:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
