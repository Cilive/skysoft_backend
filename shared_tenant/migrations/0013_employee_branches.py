# Generated by Django 4.0 on 2022-01-08 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared_tenant', '0012_company_branch_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='branches',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shared_tenant.branches'),
        ),
    ]