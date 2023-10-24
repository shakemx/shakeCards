from django.contrib import admin

from company.models import Company
from contact.models import Card

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_filter = ('is_active', )
    search_fields = ('name', )
    ordering = ('name', )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "card":
            kwargs["queryset"] = Card.objects.filter(is_active=True, type='COMPANY')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    actions=['activate', 'deactivate']

    def activate(self, request, queryset):
        queryset.update(is_active=True)
    activate.short_description='Activar Empresas'

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)
    deactivate.short_description='Desactivar Empresas'

admin.site.register(Company, CompanyAdmin)

