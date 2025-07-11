# Generated by Django 5.2.1 on 2025-05-30 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0005_ceritifications"),
    ]

    operations = [
        migrations.AddField(
            model_name="ceritifications",
            name="file",
            field=models.FileField(null=True, upload_to="certifications/"),
        ),
        migrations.AlterField(
            model_name="profileinfo",
            name="image",
            field=models.ImageField(
                default="images/shelves.jpg", null=True, upload_to=""
            ),
        ),
    ]
