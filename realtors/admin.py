from django.contrib import admin

# Register your models here.
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone')
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)

