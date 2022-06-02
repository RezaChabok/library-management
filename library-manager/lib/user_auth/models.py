from django.db import models

from django.contrib.auth.models import User


class DetailUser(models.Model):

    choice_gender = (
        ('m','men'),
        ('w','women'),
    )
    userid = models.ForeignKey(User,on_delete=models.CASCADE)
    
    gender = models.CharField(max_length=1,choices=choice_gender)
    birth_day = models.DateField()
    phone = models.CharField(max_length=20)
    national_id = models.CharField(max_length=20)
    
    class Meta:
        verbose_name = 'نام کاربر'
        verbose_name_plural = 'اطلاعات کاربران'


    def __str__(self):
        def is_admin(self):
            if self.userid.is_staff is False:
             return "User"
            return "Admin"
        return f'{self.userid.username}-{is_admin(self)}'
    def gender(self):
        return f'{self.gender}'
    def phone(self):
        return f'{self.phone}'

class UserStaff(models.Model):

    userstaff = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'نام کارمند'
        verbose_name_plural = 'اطلاعات کارمندان'

    def __str__(self):
        return f'{self.userstaff}'
    
    
