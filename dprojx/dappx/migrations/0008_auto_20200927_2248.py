# Generated by Django 3.1.1 on 2020-09-27 17:18

import dappx.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dappx', '0007_jsonfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsonfile',
            name='file',
            field=models.FileField(upload_to='documents/%Y/%m/%d', validators=[dappx.validators.validate_file_extension]),
        ),
    ]
