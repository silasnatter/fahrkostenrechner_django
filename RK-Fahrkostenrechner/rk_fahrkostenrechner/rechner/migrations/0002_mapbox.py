# Generated by Django 4.0 on 2021-12-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rechner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=100)),
            ],
        ),
    ]
