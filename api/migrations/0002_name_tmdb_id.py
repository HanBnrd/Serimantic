# Generated by Django 2.0.3 on 2018-04-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='tmdb_id',
            field=models.IntegerField(default=0),
        ),
    ]