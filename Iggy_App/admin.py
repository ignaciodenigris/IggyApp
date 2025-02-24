from django.contrib import admin

from .models import Diario, Matematica, Lengua, Economia, Programacion, Extra_materia

admin.site.register(Diario)
admin.site.register(Matematica)
admin.site.register(Lengua)
admin.site.register(Extra_materia)
# Register your models here.
