from django.db import models

# Create your models here.
class Diario(models.Model):
    texto = models.TextField(null=True)
    fecha = models.DateField()  
    def __str__(self):
        return f"Fecha: {self.fecha} texto: {self.texto}"
    
class Matematica(models.Model):
    QUESTION_CHOICES = [
        ('A', 'Primer Trimestre'),
        ('B', 'Segundo Trimestre'),
        ('C', 'Tercer Trimestre'),
    ]
    tema = models.CharField(max_length = 100)
    nota = models.IntegerField()  
    answer = models.CharField(max_length=1, choices=QUESTION_CHOICES)
    def __str__(self):
        return f"Tema: {self.tema} Nota: {self.nota} Mes: {self.answer}"

class Lengua(models.Model):
    QUESTION_CHOICES = [
        ('D', 'Primer Trimestre'),
        ('E', 'Segundo Trimestre'),
        ('F', 'Tercer Trimestre'),
    ]
    temaL = models.CharField(max_length = 100)
    notaL = models.IntegerField()  
    answerL = models.CharField(max_length=1, choices=QUESTION_CHOICES)
    def __str__(self):
        return f"Tema: {self.temaL} Nota: {self.notaL} Mes: {self.answerL}"

class Economia (models.Model):
    QUESTION_CHOICES = [
        ('J', 'Primer Trimestre'),
        ('K', 'Segundo Trimestre'),
        ('L', 'Tercer Trimestre'),
    ]
    temaE = models.CharField(max_length = 100)
    notaE = models.IntegerField()  
    answerE = models.CharField(max_length=1, choices=QUESTION_CHOICES)
    def __str__(self):
        return f"Tema: {self.tema} Nota: {self.nota} Mes: {self.answer}"

class Programacion (models.Model):
    QUESTION_CHOICES = [
        ('M', 'Primer Trimestre'),
        ('N', 'Segundo Trimestre'),
        ('O', 'Tercer Trimestre'),
    ]
    temaP = models.CharField(max_length = 100)
    notaP = models.IntegerField()  
    answerP = models.CharField(max_length=1, choices=QUESTION_CHOICES)
    def __str__(self):
        return f"Tema: {self.tema} Nota: {self.nota} Mes: {self.answer}"

class Extra_materia (models.Model):
    QUESTION_CHOICES = [
        ('G', 'Primer Trimestre'),
        ('H', 'Segundo Trimestre'),
        ('I', 'Tercer Trimestre'),
    ]
    QUESTION_Materia = [
        ('Ing', 'Ingles'),
        ('Rdw', 'Reading workshop'),
        ('Gym', 'Gimnasia'),
        ('Fsi', 'Fisica'),
        ('Qim', 'Quimico'),
        ('Cat', 'Catequesis'),
        ('Glp', 'Global politics '),
        ('HstA', 'Historia Argentina '),
        ('Hsty', 'History'),
        ('Art', 'Art'),
        ('Lit', 'Literatura'),
    ]
    materia = models.CharField(max_length=5, choices=QUESTION_Materia)
    temaEx = models.CharField(max_length = 100)
    notaEx = models.IntegerField()  
    answerEx = models.CharField(max_length=1, choices=QUESTION_CHOICES)
    def __str__(self):
        return f"Tema: {self.temaEx} Nota: {self.notaEx} Mes: {self.answerEx}"



