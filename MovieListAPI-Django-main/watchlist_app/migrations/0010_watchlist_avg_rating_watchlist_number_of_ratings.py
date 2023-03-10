# Generated by Django 4.1.1 on 2022-12-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist_app", "0009_review_review_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="watchlist",
            name="avg_rating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="watchlist",
            name="number_of_ratings",
            field=models.IntegerField(default=0),
        ),
    ]
