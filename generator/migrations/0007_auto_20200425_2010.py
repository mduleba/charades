# Generated by Django 3.0.5 on 2020-04-25 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0006_auto_20200425_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='release_country',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_world',
            field=models.DateField(default=None),
        ),
    ]
