from django.contrib import admin
from . models import Contact

# Register your models here.

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display=('fullname', 'email_id', 'message')
    search_fields=('fullname', 'email_id')
