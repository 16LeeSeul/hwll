# Generated by Django 2.1.5 on 2019-03-01 13:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_portfolio_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='DATE',
            field=models.DateField(default=datetime.datetime(2019, 3, 1, 13, 12, 9, 664725, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
