# Generated by Django 5.1.3 on 2025-02-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iggy_App', '0010_ingles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Economia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temaE', models.CharField(max_length=100)),
                ('notaE', models.IntegerField()),
                ('answerE', models.CharField(choices=[('J', 'Primer Trimestre'), ('K', 'Segundo Trimestre'), ('L', 'Tercer Trimestre')], max_length=1)),
            ],
        ),
    ]
