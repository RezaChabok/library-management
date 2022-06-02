from django.contrib import admin

from .models import borrower_details

@admin.register(borrower_details)
class AdminBrrower(admin.ModelAdmin):

    list_display = ('id','__str__','userstaff','isbn','userid')
