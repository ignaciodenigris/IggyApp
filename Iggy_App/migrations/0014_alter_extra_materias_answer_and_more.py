# Generated by Django 5.1.3 on 2025-02-08 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iggy_App', '0013_extra_materias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra_materias',
            name='answer',
            field=models.CharField(choices=[('G', 'Primer Trimestre'), ('H', 'Segundo Trimestre'), ('I', 'Tercer Trimestre')], max_length=1),
        ),
        migrations.AlterField(
            model_name='extra_materias',
            name='materia',
            field=models.CharField(choices=[('Ing', 'Ingles'), ('Rdw', 'Reading workshop'), ('Gym', 'Gimnasia'), ('Fsi', 'Fisica'), ('Qim', 'Quimico'), ('Cat', 'Catequesis'), ('Glp', 'Global politics '), ('HstA', 'Historia Argentina '), ('Hsty', 'History'), ('Art', 'Art'), ('Lit', 'Literatura')], max_length=5),
        ),
    ]
