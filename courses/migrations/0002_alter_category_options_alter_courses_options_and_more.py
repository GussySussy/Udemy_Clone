# Generated by Django 5.0.6 on 2024-07-09 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'Subcategories'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield'),
        ),
    ]
