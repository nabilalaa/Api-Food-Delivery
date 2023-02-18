from dataclasses import fields
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
        extra_kwargs = {'name': {'required': True},
                        "phone": {'required': True}}


class Mealserializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = "__all__"
        extra_kwargs = {'image': {'required': False}}
