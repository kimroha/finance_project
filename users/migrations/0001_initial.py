# Generated by Django 5.1.2 on 2024-11-01 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
    ]