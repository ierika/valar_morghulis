# Generated by Django 2.1.4 on 2019-04-23 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Alias',
                'verbose_name_plural': 'Aliases',
            },
        ),
        migrations.CreateModel(
            name='DeathCause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Unknown', 'Unknown')], max_length=20)),
                ('is_dead', models.BooleanField(default=False)),
                ('nature_of_death', models.CharField(blank=True, choices=[('homicide', 'homicide'), ('suicide', 'suicide'), ('nature causes', 'nature causes')], max_length=20, null=True)),
                ('sibling_order', models.PositiveIntegerField(default=0)),
                ('cause_of_death', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='person.DeathCause')),
                ('father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='self_father', to='person.Person')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.House')),
                ('mother', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='self_mother', to='person.Person')),
                ('murdered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='self_murdered_by', to='person.Person')),
                ('spouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='self_spouse', to='person.Person')),
            ],
            options={
                'ordering': ['house', 'sibling_order'],
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='alias',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Person'),
        ),
    ]
