# Generated by Django 4.1 on 2022-08-25 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("administration", "0002_alter_project_number_of_students"),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="collegeusers",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="administration.project",
            ),
        ),
    ]
