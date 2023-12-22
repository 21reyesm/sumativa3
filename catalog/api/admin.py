from django.contrib import admin
from .models import Provider, Service, Contact, Address

# Register your models here.
admin.site.register(Provider)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Address)
