from django.contrib import admin

from .models import ColorCompany


class ColorCompanyAdmin(admin.ModelAdmin):
    list_display = ('template', 'description','is_active')
    list_filter = ('is_active', )
    search_fields = ('template', )
    ordering = ('template', )


    actions=['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)
    activate.short_description='Activar Template'

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
    deactivate.short_description='Desactivar Template'
   
    
admin.site.register(ColorCompany, ColorCompanyAdmin)