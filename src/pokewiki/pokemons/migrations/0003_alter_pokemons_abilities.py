# Generated by Django 3.2.4 on 2021-07-14 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons', '0002_auto_20210712_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemons',
            name='abilities',
            field=models.CharField(max_length=100),
        ),
    ]
