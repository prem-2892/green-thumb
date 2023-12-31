# Generated by Django 4.2.6 on 2023-10-06 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("GreenThumb", "0003_company_company_sector"),
    ]

    operations = [
        migrations.CreateModel(
            name="ElectricityBudget",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("budget", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="EmployeeCount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="MarketSegment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="NaturalGasBudget",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("budget", models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name="company",
        ),
    ]
