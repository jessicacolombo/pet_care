# Generated by Django 4.1.6 on 2023-02-09 21:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0008_alter_pet_weight"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="weight",
            field=models.FloatField(),
        ),
    ]