# Generated by Django 4.0.4 on 2022-05-10 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='hydro',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='pizza',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]
