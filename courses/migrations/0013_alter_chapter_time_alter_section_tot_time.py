# Generated by Django 5.0.7 on 2024-07-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_alter_chapter_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='section',
            name='tot_time',
            field=models.IntegerField(default=0, verbose_name='total time taken to complete the section'),
        ),
    ]