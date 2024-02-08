from rest_framework import serializers
from .models import Usuario, Alumno, Instructor, Piscina, Curso, Inscripcion, BoletaPago, Reserva

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class PiscinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Piscina
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'

class BoletaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoletaPago
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
