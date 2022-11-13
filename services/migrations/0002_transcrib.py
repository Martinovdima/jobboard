# Generated by Django 4.1.3 on 2022-11-10 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transcrib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('pathFile', models.CharField(max_length=256)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
