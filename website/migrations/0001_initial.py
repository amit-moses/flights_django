# Generated by Django 4.2.3 on 2023-07-18 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_from', models.CharField(max_length=100)),
                ('flight_to', models.CharField(max_length=100)),
                ('airline', models.CharField(max_length=200)),
                ('tickets', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
