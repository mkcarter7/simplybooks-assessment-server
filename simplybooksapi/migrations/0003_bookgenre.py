# Generated by Django 4.1.3 on 2025-01-14 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simplybooksapi', '0002_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookgenres', to='simplybooksapi.book')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genrebooks', to='simplybooksapi.genre')),
            ],
        ),
    ]
