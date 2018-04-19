# Generated by Django 2.0.4 on 2018-04-18 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_translated'),
        ('translator', '0003_remove_translator_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='translator',
            name='direction',
            field=models.ManyToManyField(to='orders.Direction'),
        ),
    ]