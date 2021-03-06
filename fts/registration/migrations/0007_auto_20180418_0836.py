# Generated by Django 2.0.4 on 2018-04-18 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_remove_group_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='group',
        ),
        migrations.RemoveField(
            model_name='client',
            name='tags',
        ),
        migrations.AddField(
            model_name='client',
            name='completed_orders',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='client',
            name='rating',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='client',
            name='refused_orders',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
