# Generated by Django 5.0.6 on 2024-06-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A', '0002_alter_car_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('coach', models.CharField(max_length=100)),
                ('price', models.SmallIntegerField()),
            ],
        ),
    ]
