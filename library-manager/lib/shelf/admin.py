from django.contrib import admin
from .models import shelf_details



@admin.register(shelf_details)
class AdminDetailShelf(admin.ModelAdmin):

    list_display = ('id','isbn','serial_code','shelf','corridor')
    
