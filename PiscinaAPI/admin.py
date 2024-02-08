from django.contrib import admin
from .models import Usuario, Alumno, Instructor, Piscina, Curso, Inscripcion, BoletaPago, Reserva


admin.site.register(Usuario)
admin.site.register(Alumno)
admin.site.register(Instructor)
admin.site.register(Piscina)
admin.site.register(Curso)
admin.site.register(Inscripcion)
admin.site.register(BoletaPago)
admin.site.register(Reserva)