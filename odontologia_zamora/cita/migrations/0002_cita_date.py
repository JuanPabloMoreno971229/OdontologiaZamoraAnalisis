# Generated by Django 4.0.4 on 2022-05-01 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='date',
            field=models.DateTimeField(default=2, verbose_name='Fecha de la cita'),
            preserve_default=False,
        ),
    ]
