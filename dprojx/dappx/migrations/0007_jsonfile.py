# Generated by Django 3.1.1 on 2020-09-27 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0006_auto_20200927_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='JsonFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
