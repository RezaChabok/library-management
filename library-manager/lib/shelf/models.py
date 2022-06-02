from django.db import models
from books.models import book_manager



class shelf_details(models.Model):

    serial_code = models.CharField(max_length=17,unique=True)
    isbn = models.ForeignKey(book_manager,on_delete=models.CASCADE)
    shelf = models.IntegerField()
    corridor = models.IntegerField()    
    class Meta:
        verbose_name = 'آدرس کتاب'
        verbose_name_plural = 'ادرس کتاب ها'

    def __str__(self):
        return f'{self.isbn}'
    

    



