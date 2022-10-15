from django.contrib import admin
from .models import Car
from django.utils.html import format_html


class CarAdmin(admin.ModelAdmin):

    list_display = ('id','car_title', 'is_featured','car_photo')
    list_display_links = ('id', )
    list_editable = ('is_featured','car_photo','car_title')
    search_fields = ('id', 'car_title', 'car_title', 'city', 'model', 'body_style','fuel_type')
    list_filter = ('city', 'model', 'body_style', 'fuel_type')

    actions = ['duplicate_event']
    def duplicate_event(modeladmin, request, queryset):
        for object in queryset:
            object.id = None
            object.save()
    duplicate_event.short_description = "Duplicate selected record"

admin.site.register(Car, CarAdmin)



