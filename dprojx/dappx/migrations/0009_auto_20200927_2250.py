# Generated by Django 3.1.1 on 2020-09-27 17:20

import dappx.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0008_auto_20200927_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsonfile',
            name='file',
            field=models.FileField(upload_to='', validators=[dappx.validators.validate_file_extension]),
        ),
    ]
