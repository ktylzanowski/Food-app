# Generated by Django 4.2.2 on 2023-06-20 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
