from django.contrib import admin

from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active', )
    search_fields = ('name', )
    ordering = ('name', )

    actions=['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)
    activate.short_description='Activar Servicio'

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
    deactivate.short_description='Desactivar Servicio'

admin.site.register(Service, ServiceAdmin)


