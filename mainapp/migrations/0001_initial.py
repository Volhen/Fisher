# Generated by Django 3.0.2 on 2020-03-07 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='название')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='название товара')),
                ('image', models.ImageField(blank=True, upload_to='products_images')),
                ('short_desc', models.CharField(blank=True, max_length=129, verbose_name='краткое описание товара')),
                ('description', models.TextField(blank=True, verbose_name='описание товара')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена товара')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество на складе')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductCategory')),
            ],
        ),
    ]