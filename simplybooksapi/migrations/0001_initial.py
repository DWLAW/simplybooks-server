# Generated by Django 4.1.3 on 2025-01-11 16:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('image', models.URLField()),
                ('favorite', models.BooleanField()),
                ('uid', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('sale', models.BooleanField()),
                ('uid', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=280)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='simplybooksapi.author')),
            ],
        ),
    ]
