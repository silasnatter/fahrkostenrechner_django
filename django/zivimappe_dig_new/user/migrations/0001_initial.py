# Generated by Django 3.2.7 on 2021-09-28 10:28

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('profile_pic', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='user')),
                ('bio', models.CharField(blank=True, max_length=255)),
                ('beginn', models.DateField()),
                ('end', models.DateField()),
                ('birthdate', models.DateField()),
                ('nickname', models.CharField(blank=True, max_length=250)),
                ('short_text', models.TextField(blank=True, null=True)),
                ('img_1', models.ImageField(blank=True, null=True, upload_to='img_uploaded/')),
                ('img_2', models.ImageField(blank=True, null=True, upload_to='img_uploaded/')),
                ('img_3', models.ImageField(blank=True, null=True, upload_to='img_uploaded/')),
                ('vid_1', models.FileField(blank=True, null=True, upload_to='vid_uploaded/')),
            ],
        ),
    ]
