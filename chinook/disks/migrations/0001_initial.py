# Generated by Django 5.2 on 2025-04-09 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disks.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('composer', models.CharField(max_length=200, null=True)),
                ('milliseconds', models.IntegerField(verbose_name='Duration (ms)')),
                ('bytes', models.IntegerField(verbose_name='Size (bytes)')),
                ('unitPrice', models.FloatField(verbose_name='Unit Price (EUR)')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disks.album')),
            ],
        ),
    ]
