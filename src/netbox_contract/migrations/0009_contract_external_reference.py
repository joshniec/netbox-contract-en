# Generated by Django 4.1.5 on 2023-01-22 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_contract", "0008_invoice_comments"),
    ]

    operations = [
        migrations.AddField(
            model_name="contract",
            name="external_reference",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
