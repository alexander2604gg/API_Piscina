from rest_framework import viewsets
from .models import Usuario, Alumno, Instructor, Piscina, Curso, Inscripcion, BoletaPago, Reserva
from .serializer import UsuarioSerializer, AlumnoSerializer, InstructorSerializer, PiscinaSerializer, CursoSerializer, InscripcionSerializer, BoletaPagoSerializer, ReservaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class PiscinaViewSet(viewsets.ModelViewSet):
    queryset = Piscina.objects.all()
    serializer_class = PiscinaSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer

class BoletaPagoViewSet(viewsets.ModelViewSet):
    queryset = BoletaPago.objects.all()
    serializer_class = BoletaPagoSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

