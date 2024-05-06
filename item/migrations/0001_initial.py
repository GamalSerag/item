# Generated by Django 5.0.1 on 2024-05-06 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItemExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255)),
                ('extras', models.ManyToManyField(blank=True, to='item.menuitemextra')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItemExtraItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('extra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='item.menuitemextra')),
            ],
        ),
    ]