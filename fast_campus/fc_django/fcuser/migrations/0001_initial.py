# Generated by Django 3.2 on 2021-10-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fcuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Field ')),
                ('password', models.CharField(max_length=20, verbose_name='Password Name ')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='Registered Date ')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'fastcampus_user',
            },
        ),
    ]