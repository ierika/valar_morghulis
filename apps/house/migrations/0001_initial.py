# Generated by Django 2.1.4 on 2019-04-23 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('sigil_description', models.TextField(blank=True, null=True)),
                ('sigil_image_url', models.URLField(blank=True, null=True)),
                ('motto', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.Region')),
            ],
            options={
                'ordering': ['name', 'region'],
            },
        ),
    ]
