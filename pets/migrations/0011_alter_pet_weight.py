# Generated by Django 4.1.6 on 2023-02-09 22:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0010_alter_pet_weight"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="weight",
            field=models.FloatField(),
        ),
    ]
