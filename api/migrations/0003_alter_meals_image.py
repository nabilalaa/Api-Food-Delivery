# Generated by Django 4.1.3 on 2022-11-27 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_meals_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='image',
            field=models.ImageField(upload_to='resturant'),
        ),
    ]
