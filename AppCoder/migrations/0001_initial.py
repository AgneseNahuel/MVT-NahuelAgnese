# Generated by Django 4.1 on 2022-11-17 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('DNI', models.IntegerField()),
                ('fechadecumpleaños', models.DateField()),
            ],
        ),
    ]
