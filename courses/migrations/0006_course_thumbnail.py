# Generated by Django 5.0.6 on 2024-07-10 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_rename_courses_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='thumbnail',
            field=models.ImageField(default=None, upload_to='thumbnails/<django.db.models.fields.UUIDField>'),
            preserve_default=False,
        ),
    ]
