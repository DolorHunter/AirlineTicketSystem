# Generated by Django 3.0.8 on 2020-08-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_auto_20200805_2149'),
        ('TicketApp', '0005_auto_20200814_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookticketitem',
            name='ticket_id',
        ),
        migrations.RemoveField(
            model_name='bookticketitem',
            name='user_id',
        ),
        migrations.AddField(
            model_name='bookticketitem',
            name='ticket',
            field=models.ManyToManyField(to='TicketApp.TicketItem'),
        ),
        migrations.AddField(
            model_name='bookticketitem',
            name='user',
            field=models.ManyToManyField(to='UserApp.UserItem'),
        ),
    ]
