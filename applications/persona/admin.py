from django.contrib import admin
from .models import Empleado,Habilidades

# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    
    def full_name(self,obj):
        print (obj)
        return (obj.first_name + ' + ' + obj.last_name)    
    
    list_display = (
                    'id',
                    'first_name',
                    'last_name',
                    'full_name',
                    'job',
                    'avatar'
                    )
    
    list_filter = ('job',
                   'habilidades',
                   )
    
    search_fields = ('job',
                    )
    
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado,EmpleadoAdmin)
