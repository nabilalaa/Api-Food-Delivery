# Generated by Django 4.1.3 on 2022-12-10 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_meals_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='image',
            field=models.ImageField(blank=0, default='null', upload_to='resturant'),
        ),
    ]
