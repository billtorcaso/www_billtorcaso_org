# Generated by Django 3.0.6 on 2020-05-19 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BTOPage", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="btoinfosnippet",
            name="info",
            field=models.CharField(
                blank=True, default="William D. Torcaso", max_length=256, null=True
            ),
        ),
    ]
