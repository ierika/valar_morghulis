# Generated by Django 2.1.4 on 2019-04-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='motto',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
