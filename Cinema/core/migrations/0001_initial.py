# Generated by Django 4.2.7 on 2025-07-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('poster', models.CharField(max_length=255)),
            ],
        ),
    ]
