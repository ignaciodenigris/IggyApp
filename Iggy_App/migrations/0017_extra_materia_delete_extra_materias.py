# Generated by Django 5.1.3 on 2025-02-08 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Iggy_App', '0016_rename_answer_extra_materias_answerex_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extra_materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(choices=[('Ing', 'Ingles'), ('Rdw', 'Reading workshop'), ('Gym', 'Gimnasia'), ('Fsi', 'Fisica'), ('Qim', 'Quimico'), ('Cat', 'Catequesis'), ('Glp', 'Global politics '), ('HstA', 'Historia Argentina '), ('Hsty', 'History'), ('Art', 'Art'), ('Lit', 'Literatura')], max_length=5)),
                ('temaEx', models.CharField(max_length=100)),
                ('notaEx', models.IntegerField()),
                ('answerEx', models.CharField(choices=[('G', 'Primer Trimestre'), ('H', 'Segundo Trimestre'), ('I', 'Tercer Trimestre')], max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Extra_materias',
        ),
    ]
