# Generated by Django 5.0.6 on 2024-07-08 19:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Programmer",
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
                ("fullname", models.CharField(max_length=100)),
                ("nickname", models.CharField(max_length=50)),
                ("age", models.PositiveSmallIntegerField()),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]
