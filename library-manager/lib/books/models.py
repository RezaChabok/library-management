from category.models import Category
from django.db import models
class BookManager(models.Manager):
    def get_status(self, query):
        return self.get_queryset().filter(book_title__icontains = query ).distinct()

class book_manager(models.Model):


    choice_status = (   
        ('ناموجود','ناموجود'),
        ('موجود','موجود'),
    )

    isbn = models.CharField(max_length=13,unique=True)
    book_title = models.CharField(max_length=8)
    lang = models.CharField(max_length=5)
    book_status = models.CharField(max_length=10,choices=choice_status )
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pub_year = models.DateField()
    objects = BookManager()
    class Meta:
        verbose_name = 'نام کتاب'
        verbose_name_plural = 'کتاب ها'

    def __str__(self):
        return f'{self.isbn}'       

