# Generated by Django 3.0.5 on 2020-12-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('DOB', models.CharField(max_length=15)),
                ('Gender', models.CharField(max_length=10)),
                ('Mobile', models.IntegerField(max_length=20, unique=True)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('category', models.CharField(default='Mobile', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('DOB', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=10)),
                ('Mobile', models.IntegerField(max_length=20, unique=True)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
