# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-08 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locality', models.CharField(choices=[('Toluca de Lerdo', 'Toluca'), ('Metepec', 'Metepec')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(choices=[('Estado de Mexico', 'Estado de Mexico')], max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='address',
            name='colonia',
        ),
        migrations.RemoveField(
            model_name='address',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='address',
            name='number',
        ),
        migrations.RemoveField(
            model_name='address',
            name='other_address_reference',
        ),
        migrations.RemoveField(
            model_name='address',
            name='state',
        ),
        migrations.RemoveField(
            model_name='address',
            name='street',
        ),
        migrations.AddField(
            model_name='address',
            name='address_line_1',
            field=models.CharField(default='No addres', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='address',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='address',
            name='address_line_3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='locality',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Region'),
        ),
        migrations.AddField(
            model_name='address',
            name='locality',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='places.Locality'),
            preserve_default=False,
        ),
    ]
