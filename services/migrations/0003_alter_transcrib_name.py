# Generated by Django 3.2.3 on 2022-11-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_transcrib_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transcrib',
            name='name',
            field=models.CharField(default='default name', max_length=256),
        ),
    ]
