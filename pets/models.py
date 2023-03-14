from django.db import models

# Create your models here.


class SexFields(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    DEFAULT = "Not Informed"


class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=20, choices=SexFields.choices, default=SexFields.DEFAULT
    )

    group = models.ForeignKey(
        "groups.Group", on_delete=models.PROTECT, related_name="pets"
    )

    traits = models.ManyToManyField("traits.Trait", related_name="traits")
