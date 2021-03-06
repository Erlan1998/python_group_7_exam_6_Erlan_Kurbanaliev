from django.contrib import admin

from webapp.models import Guest


# Register your models here.

class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mail', 'date_creat', 'date_update']
    list_filter = ['date_creat']
    search_fields = ['mail', 'date_creat']
    fields = ['id', 'name', 'mail', 'description']
    readonly_fields = ['id', 'date_update']

admin.site.register(Guest, GuestAdmin)
