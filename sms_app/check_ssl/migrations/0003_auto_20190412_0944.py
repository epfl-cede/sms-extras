# Generated by Django 2.2 on 2019-04-12 09:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('check_ssl', '0002_auto_20190412_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
