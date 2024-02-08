from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, AlumnoViewSet, InstructorViewSet, PiscinaViewSet, CursoViewSet, InscripcionViewSet, BoletaPagoViewSet, ReservaViewSet

# Creamos un router
router = DefaultRouter()

# Registramos los ViewSets con el router
router.register(r'usuarios', UsuarioViewSet)
router.register(r'alumnos', AlumnoViewSet)
router.register(r'instructores', InstructorViewSet)
router.register(r'piscinas', PiscinaViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'inscripciones', InscripcionViewSet)
router.register(r'boletas-pago', BoletaPagoViewSet)
router.register(r'reservas', ReservaViewSet)

# Definimos las URLs
urlpatterns = [
    path('', include(router.urls)),
]
