from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProviderViewSet, ServiceViewSet, AddressViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'proveedores', ProviderViewSet, basename='proveedor')
router.register(r'servicios', ServiceViewSet, basename='servicio')
router.register(r'direcciones', AddressViewSet, basename='dirección')
router.register(r'contactos', ContactViewSet, basename='contacto')

urlpatterns = [
    path('', include(router.urls)),
]
