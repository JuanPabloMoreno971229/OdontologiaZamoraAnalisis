from cita.models import cita
from django.contrib import admin

# Register your models here.
class citaAdmin(admin.ModelAdmin):
    #readonly_fields = ('procedure','name', 'mail', 'phone', 'message', 'created')
    list_filter = ('procedure', 'status')
    list_display = ('name','procedure', 'status')

admin.site.register(cita, citaAdmin)