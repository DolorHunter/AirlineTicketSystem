# Generated by Django 3.0.8 on 2020-08-05 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TicketApp', '0002_auto_20200805_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketitem',
            name='flight_income',
        ),
    ]