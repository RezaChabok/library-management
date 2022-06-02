from django.contrib import admin

from .models import book_manager


@admin.register(book_manager)
class Adminbookmanager(admin.ModelAdmin):

    list_display = ('id','book_title','isbn','lang','book_status','category','pub_year',)
