# Generated by Django 3.1.1 on 2020-10-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketApp', '0009_auto_20201024_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookticketitem',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
