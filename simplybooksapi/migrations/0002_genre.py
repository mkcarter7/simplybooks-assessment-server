# Generated by Django 4.1.3 on 2025-01-14 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplybooksapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]
