# Generated by Django 4.2.2 on 2023-08-30 10:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todotask",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
