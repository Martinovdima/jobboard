# Generated by Django 4.1.3 on 2022-11-10 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_transcrib'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transcrib',
            name='pathFile',
        ),
        migrations.AddField(
            model_name='transcrib',
            name='audio',
            field=models.FileField(blank=True, upload_to='audio'),
        ),
    ]
