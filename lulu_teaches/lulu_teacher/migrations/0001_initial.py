# Generated by Django 5.1.2 on 2024-10-11 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='historicalSessions',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('sessionDate', models.DateTimeField(verbose_name='session date')),
                ('username', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]