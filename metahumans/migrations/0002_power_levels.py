# Generated by Django 3.0.5 on 2020-04-30 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metahumans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='power',
            name='levels',
            field=models.IntegerField(default=50),
        ),
    ]
