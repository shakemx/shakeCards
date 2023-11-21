from django.contrib import admin

from tool.models import Utility

class UtilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type','is_active')
    list_filter = ('name','type', )
    search_fields = ('name', )
    ordering = ('name', )

    actions=['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)
    activate.short_description='Activar Utileria'

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
    deactivate.short_description='Desactivar Utileria'

admin.site.register(Utility, UtilityAdmin)
