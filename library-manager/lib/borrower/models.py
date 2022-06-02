
from django.db import models
from books.models import book_manager
from user_auth.models import DetailUser,UserStaff

# from books.models import book
class BorrowerManager(models.Manager):
    def search(self, query1,query2):
        return self.get_queryset().filter(borrowed_from__gte = query1 ,borrowed_to__lte = query2).distinct()

class borrower_details(models.Model):

    userid = models.ForeignKey(DetailUser,on_delete=models.CASCADE)
    userstaff = models.ForeignKey(UserStaff,on_delete=models.CASCADE)
    isbn = models.ForeignKey(book_manager,on_delete=models.CASCADE)
    borrowed_from = models.DateField(null=True,blank=True)
    borrowed_to  = models.DateField(null=True,blank=True)
    objects = BorrowerManager()
    class Meta:
        verbose_name = 'تراکنش'
        verbose_name_plural = 'تراکنش ها'
    
    def __str__(self):
        def is_admin(self):
            if self.userid.userid.is_staff is False:
             return "User"
            return "Admin"
        return f'{self.userid}-{is_admin(self)}'

