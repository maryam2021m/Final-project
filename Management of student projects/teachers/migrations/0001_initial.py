# Generated by Django 4.1 on 2022-08-25 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProjectSetting",
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
                ("can_get", models.BooleanField()),
                ("suggest", models.BooleanField()),
                ("reports", models.BooleanField()),
                ("final_report", models.BooleanField()),
            ],
        ),
    ]