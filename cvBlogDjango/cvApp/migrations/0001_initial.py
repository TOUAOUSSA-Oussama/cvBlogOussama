# Generated by Django 3.2.9 on 2021-11-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('nomEntreprise', models.CharField(max_length=100)),
                ('dateDebut', models.CharField(max_length=100)),
                ('dateFin', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Formations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anneeDebut', models.CharField(max_length=4)),
                ('anneeFin', models.CharField(max_length=4)),
                ('description', models.CharField(max_length=400)),
                ('lieu', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('environnement', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
            ],
        ),
    ]