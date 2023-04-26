from .models import *
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination


@api_view(["GET", "POST"])
def users(request):
    search = request.GET.get("search")

    if search:
        if User.objects.filter(username__contains=search):
            serializer = Userserializer(
                User.objects.filter(username__contains=search), many=True)
            return Response(serializer.data)
        elif User.objects.filter(email__contains=search):
            serializer = Userserializer(
                User.objects.filter(email__contains=search), many=True)
            return Response(serializer.data)

        else:
            return Response([])

    if request.method == "GET":
        pagination = LimitOffsetPagination()
        pagination.count = 6
        users = User.objects.all()

        result_page = pagination.paginate_queryset(users, request)

        serializer = Userserializer(result_page, many=True)
        return pagination.get_paginated_response(serializer.data)

    if request.method == "POST":
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)


@api_view(["GET", "PUT", "DELETE"])
def user_details(request, id):

    try:
        user = User.objects.get(pk=id)

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = Userserializer(user)
        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = Userserializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user.delete()
        return Response(data="Done", status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def category(request):
    search = request.GET.get("search")

    if search:
        if Category.objects.filter(nameArabic__contains=search):
            serializer = Categoryserializer(
                Category.objects.filter(nameArabic__contains=search), many=True)
            return Response(serializer.data)

        else:
            return Response([])

    if request.method == "GET":
        categories = Category.objects.all()
        serializer = Categoryserializer(categories, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = Categoryserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def category_details(request, id):

    try:
        category = Category.objects.get(pk=id)

    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = Categoryserializer(category)
        return Response(serializer.data)

    elif request.method == "PUT":

        serializer = Categoryserializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        category.delete()
        return Response(data="Done", status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def order(request):
    search = request.GET.get("search")

    if search:
        if Order.objects.filter(name__contains=search):
            serializer = Orderserializer(
                Order.objects.filter(name__contains=search), many=True)
            return Response(serializer.data)

        elif Order.objects.filter(address__contains=search):
            serializer = Orderserializer(
                Order.objects.filter(address__contains=search), many=True)
            return Response(serializer.data)

        elif Order.objects.filter(number__contains=search):
            serializer = Orderserializer(
                Order.objects.filter(number__contains=search), many=True)
            return Response(serializer.data)

        elif Order.objects.filter(email__contains=search):
            serializer = Orderserializer(
                Order.objects.filter(email__contains=search), many=True)
            return Response(serializer.data)

        else:
            return Response([])

    if request.method == "GET":
        orders = Order.objects.all()
        serializer = Orderserializer(orders, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = Orderserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)


@api_view(["GET", "PUT", "DELETE"])
def order_details(request, id):
    try:
        order = Order.objects.get(pk=id)

    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = Orderserializer(order)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = Orderserializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

    elif request.method == "DELETE":
        order.delete()
        return Response(data="Done", status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def meal(request):
    search = request.GET.get("search")

    if search:
        if Meal.objects.filter(name__contains=search):
            serializer = Mealserializer(
                Meal.objects.filter(name__contains=search), many=True)
            return Response(serializer.data)

        else:
            return Response([])

    if request.method == "GET":
        pagination = LimitOffsetPagination()
        meals = Meal.objects.all()
        result_page = pagination.paginate_queryset(meals, request)

        serializer = Mealserializer(result_page, many=True)
        return pagination.get_paginated_response(serializer.data)

    if request.method == "POST":
        serializer = Mealserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)


@api_view(["GET", "PUT", "DELETE"])
def meal_details(request, id):
    try:
        meal = Meal.objects.get(pk=id)

    except Meal.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = Mealserializer(meal)
        return Response(serializer.data)

    elif request.method == "PUT":
        print(request.data)
        serializer = Mealserializer(meal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

    elif request.method == "DELETE":
        meal.delete()
        return Response(data="Done", status=status.HTTP_204_NO_CONTENT)
