from django.contrib import admin

# Register your models here.
from .models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'realtor', 'price', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    search_fields = ('title', 'description', 'address', 'city', 'state')
    list_editable = ('is_published',)
    list_per_page = 25

admin.site.register(Property, PropertyAdmin)


