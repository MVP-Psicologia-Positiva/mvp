# Generated by Django 5.1.2 on 2024-10-11 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lulu_teacher', '0002_delete_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsessions',
            name='ID',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
