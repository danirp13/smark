# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 03:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProductos',
            fields=[
                ('id_categoria', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=80, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=80, null=True)),
                ('cantidad', models.BigIntegerField(blank=True, null=True)),
                ('precio', models.BigIntegerField(blank=True, null=True)),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
                ('id_categoria', models.ForeignKey(blank=True, db_column='id_categoria', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.CategoriaProductos')),
            ],
        ),
    ]