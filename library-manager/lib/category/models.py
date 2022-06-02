from django.db import models


class Category(models.Model):

    title = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'موضوع'
        verbose_name_plural = 'موضوعات'

    def __str__(self):
        return f'{self.title}'
    
