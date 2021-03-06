# Generated by Django 2.1.1 on 2018-09-27 10:59

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 9, 27, 10, 59, 16, 351670, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('sub_title', models.CharField(blank=True, max_length=30)),
                ('contents', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 9, 27, 10, 59, 16, 350224, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete='CASCADE', to='blog.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
