# Generated by Django 3.2.9 on 2021-11-23 22:34

from django.db import migrations, models

import utils.forms.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Relationship",
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
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated", models.DateTimeField(auto_now=True, null=True)),
                ("name", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField(max_length=100, unique=True)),
                ("description", models.CharField(blank=True, max_length=200)),
                (
                    "color",
                    utils.forms.fields.ColourField(default="9e9e9e", max_length=6),
                ),
            ],
            options={"ordering": ["name"]},
        ),
    ]
