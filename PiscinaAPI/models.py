from django.db import models

class Usuario(models.Model):
    UsuarioID = models.AutoField(primary_key=True)
    NombreUsuario = models.CharField(max_length=50, null=True)
    Correo = models.EmailField(max_length=100, null=True)
    Contraseña = models.CharField(max_length=50, null=True)
    Tipo = models.CharField(max_length=15, null=True)

class Alumno(models.Model):
    Dni = models.CharField(max_length=15, primary_key=True)
    Nombre = models.CharField(max_length=30, null=True)
    Apellido = models.CharField(max_length=40, null=True)
    Celular = models.CharField(max_length=9, null=True)
    UsuarioID = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)

class Instructor(models.Model):
    InstructorID = models.AutoField(primary_key=True)
    Dni = models.CharField(max_length=15, null=True)
    Nombre = models.CharField(max_length=50, null=True)
    Apellido = models.CharField(max_length=50, null=True)
    Email = models.EmailField(max_length=100, null=True)
    Celular = models.CharField(max_length=9, null=True)
    UsuarioID = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)
    PagoMensual = models.FloatField(null=True)

class Piscina(models.Model):
    PiscinaID = models.AutoField(primary_key=True)
    Nivel = models.CharField(max_length=15, null=True)
    Precio = models.FloatField(null=True)

class Curso(models.Model):
    CursoID = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=True)
    CostoMensual = models.FloatField(null=True)
    InstructorID = models.ForeignKey(Instructor, null=True, on_delete=models.CASCADE)

class Inscripcion(models.Model):
    Dni = models.CharField(max_length=15, primary_key=True)
    CursoID = models.ForeignKey(Curso, on_delete=models.CASCADE)
    Descuento = models.FloatField(null=True)
    FechaInscripcion = models.DateField(null=True)

class BoletaPago(models.Model):
    BoletaPagoID = models.AutoField(primary_key=True)
    Monto = models.FloatField(null=True)
    MetodoPago = models.CharField(max_length=12, null=True)
    FechaPago = models.DateField(null=True)
    Dni = models.CharField(max_length=15)
    CursoID = models.ForeignKey(Curso, on_delete=models.CASCADE)

class Reserva(models.Model):
    ReservaID = models.AutoField(primary_key=True)
    UsuarioID = models.ForeignKey(Usuario, null=True, on_delete=models.CASCADE)
    PiscinaID = models.ForeignKey(Piscina, null=True, on_delete=models.CASCADE)
    FechaInicio = models.DateField(null=True)
    FechaTermino = models.DateField(null=True)
    FechaReserva = models.DateField(null=True)


