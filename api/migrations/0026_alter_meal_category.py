# Generated by Django 4.1.7 on 2023-04-22 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_alter_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.category'),
        ),
    ]
