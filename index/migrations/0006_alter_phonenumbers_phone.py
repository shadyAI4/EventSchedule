# Generated by Django 4.0.2 on 2024-05-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_phonenumbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumbers',
            name='phone',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]