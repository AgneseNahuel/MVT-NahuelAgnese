# Generated by Django 4.1 on 2022-11-17 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='fechadecumpleaños',
            field=models.DateField(max_length=50),
        ),
    ]
