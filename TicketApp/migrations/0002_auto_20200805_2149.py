# Generated by Django 3.0.8 on 2020-08-05 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TicketApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TicketAppItem',
            new_name='TicketItem',
        ),
    ]
