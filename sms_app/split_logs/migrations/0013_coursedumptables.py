# Generated by Django 2.2 on 2019-05-09 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('split_logs', '0012_auto_20190509_0902'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDumpTables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('primary_key', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
