# Generated by Django 4.2.6 on 2023-10-06 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("GreenThumb", "0007_rename_marketsegment_companysector_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="annual_natural_gas_budget",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="companies_by_gas_budget",
                to="GreenThumb.naturalgasbudget",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="company_sector",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="companies_by_sector",
                to="GreenThumb.companysector",
            ),
        ),
        migrations.CreateModel(
            name="Program",
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
                ("program_name", models.CharField(max_length=100)),
                ("link", models.URLField()),
                ("project_type", models.CharField(max_length=50)),
                ("supporting_docs", models.TextField()),
                ("description", models.TextField()),
                (
                    "annual_electricity_budget",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="programs_by_electricity_budget",
                        to="GreenThumb.electricitybudget",
                    ),
                ),
                (
                    "annual_natural_gas_budget",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="programs_by_gas_budget",
                        to="GreenThumb.naturalgasbudget",
                    ),
                ),
                (
                    "company_sector",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="programs_by_sector",
                        to="GreenThumb.companysector",
                    ),
                ),
                (
                    "employee_count",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="programs_by_employee_count",
                        to="GreenThumb.employeecount",
                    ),
                ),
            ],
        ),
    ]
