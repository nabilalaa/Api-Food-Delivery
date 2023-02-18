from django.urls import path

from .views import *
urlpatterns = [
    path("admins", users),
    path("admins/<int:id>", user_details),
    path("category", category),
    path("category/<int:id>", category_details),
    path("order", order),
    path("order/<int:id>", order_details),
    path("meal", meal),
    path("meal/<int:id>", meal_details),
]
