# Generated by Django 5.1.3 on 2025-01-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iggy_App', '0002_rename_competencias_diario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_actual', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
