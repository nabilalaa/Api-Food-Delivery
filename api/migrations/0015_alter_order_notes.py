# Generated by Django 4.1.3 on 2023-02-18 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_order_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='notes',
            field=models.TextField(blank=0, null=1),
        ),
    ]
