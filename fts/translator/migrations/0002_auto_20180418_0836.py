# Generated by Django 2.0.4 on 2018-04-18 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180418_0836'),
        ('translator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='translator',
            name='busy',
            field=models.CharField(default='0', max_length=5),
        ),
        migrations.AddField(
            model_name='translator',
            name='direction',
            field=models.ManyToManyField(to='orders.Direction'),
        ),
    ]
