# Generated by Django 4.1.1 on 2022-09-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
