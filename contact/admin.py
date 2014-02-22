from django.contrib import admin

from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['subject', 'email', 'created']
    search_fields = ['subject', 'email', 'content']
    list_filter = ['created', 'email']


admin.site.register(Contact, ContactAdmin)