# Generated by Django 5.1.4 on 2024-12-10 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_user_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
    ]