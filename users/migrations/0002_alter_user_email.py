# Generated by Django 5.0.6 on 2024-07-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=True, max_length=254, unique=True),
        ),
    ]
