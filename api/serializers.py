from unicodedata import category
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class Orderserializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class Mealserializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.nameEnglish")

    class Meta:
        model = Meal
        fields = "__all__"
