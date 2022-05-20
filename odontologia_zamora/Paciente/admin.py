from pydoc import Doc, doc
from django.contrib import admin
from Paciente.models import paciente
from .models import paciente


class PacienteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_filter = ('name','phone')
    list_display = ('name','email')

admin.site.register(paciente, PacienteAdmin)