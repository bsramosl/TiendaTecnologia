# Generated by Django 3.2.9 on 2023-02-15 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Imagen1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Imagen2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Imagen3')),
                ('stock', models.IntegerField(verbose_name='Cantidad')),
                ('date_creation', models.DateTimeField(auto_now=True)),
                ('date_update', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashboardApp.categorymodel', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['name'],
            },
        ),
    ]