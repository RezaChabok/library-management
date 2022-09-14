from django.contrib import admin

from .models import DetailUser,UserStaff

@admin.register(DetailUser)
class AdminDetailUser(admin.ModelAdmin):
    list_display = ('__str__','id','get_gender','birth_day','get_phone','national_id')


@admin.register(UserStaff)
class AdminUserStaff(admin.ModelAdmin):
    list_display = ('id','__str__',)
    
    
