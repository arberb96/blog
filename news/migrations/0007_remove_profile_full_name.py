# Generated by Django 4.2 on 2024-05-28 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0006_profile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="full_name",
        ),
    ]
