# Generated by Django 4.1.3 on 2023-02-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_meals_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='nameArabic',
            field=models.CharField(max_length=40, null=1),
            preserve_default=1,
        ),
        migrations.AddField(
            model_name='category',
            name='nameEnglish',
            field=models.CharField(max_length=40, null=1),
            preserve_default=1,
        ),
    ]
