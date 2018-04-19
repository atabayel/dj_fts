# Generated by Django 2.0.4 on 2018-04-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20180410_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=255)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('deprecated', models.BooleanField(default=False)),
            ],
        ),
    ]
