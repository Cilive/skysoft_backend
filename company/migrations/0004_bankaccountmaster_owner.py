# Generated by Django 4.0 on 2022-01-09 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_bankaccountmaster_is_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccountmaster',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.owner'),
        ),
    ]
