# Generated by Django 4.1.5 on 2023-01-24 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_contract", "0011_auto_20230122_2112"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="invoice",
            name="contract",
        ),
    ]
