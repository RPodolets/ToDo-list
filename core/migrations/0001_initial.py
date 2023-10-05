# Generated by Django 4.2.6 on 2023-10-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("content", models.CharField(max_length=511)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateTimeField(blank=True, default="")),
                ("is_done", models.BooleanField()),
                ("tags", models.ManyToManyField(related_name="tasks", to="core.tag")),
            ],
        ),
    ]
