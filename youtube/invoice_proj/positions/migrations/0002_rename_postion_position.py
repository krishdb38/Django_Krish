# Generated by Django 3.2 on 2022-03-27 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_rename_tag_invoice_tags'),
        ('positions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Postion',
            new_name='Position',
        ),
    ]
