from django.contrib import admin
from .models import Departamento, Fotos, Favoritos, Agentes, Localidades, Usuarios

admin.site.register(Departamento)
admin.site.register(Fotos)
admin.site.register(Favoritos)
admin.site.register(Agentes)
admin.site.register(Localidades)
admin.site.register(Usuarios)

