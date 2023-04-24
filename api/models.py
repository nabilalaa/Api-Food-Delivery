from django.db import models


class Category(models.Model):
    nameArabic = models.CharField(max_length=40, null=1)
    nameEnglish = models.CharField(max_length=40, null=1)

    def __str__(self):
        return self.nameArabic


class Order(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(null=1)
    address = models.TextField(null=1)
    number = models.BigIntegerField(null=1)
    order = models.TextField(null=1)
    notes = models.TextField(null=1, blank=True)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=80)
    desc = models.TextField(null=1)
    price = models.FloatField(null=1)
    image = models.ImageField(upload_to="resturant", blank=1)
    # image = CloudinaryField("resturant")

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
