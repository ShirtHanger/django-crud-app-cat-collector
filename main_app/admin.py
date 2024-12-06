from django.contrib import admin
from .models import Cat, Feeding

# Register your models here for Admin CRUD

admin.site.register(Cat)
admin.site.register(Feeding)