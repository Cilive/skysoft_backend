# Generated by Django 4.0 on 2021-12-30 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared_tenant', '0005_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
