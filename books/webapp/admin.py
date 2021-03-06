from django.contrib import admin

from webapp.models import Guest


# Register your models here.

class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mail', 'status', 'date_creat', 'date_update']
    list_filter = ['status']
    search_fields = ['mail', 'name']
    fields = ['id', 'name', 'mail', 'description', 'status']
    readonly_fields = ['id', 'date_update']

admin.site.register(Guest, GuestAdmin)
