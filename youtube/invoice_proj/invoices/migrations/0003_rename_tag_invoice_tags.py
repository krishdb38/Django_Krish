# Generated by Django 3.2 on 2022-03-27 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20220327_1217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='tag',
            new_name='tags',
        ),
    ]
