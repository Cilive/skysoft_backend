# Generated by Django 4.0 on 2021-12-30 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared_tenant', '0003_user_is_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=False),
        ),
    ]
