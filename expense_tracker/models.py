from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Expense(models.Model):
    date = models.DateField(default=datetime.datetime.now().strftime('%Y-%m-%d'))
    time = models.TimeField(auto_now_add=True)
    debit = models.PositiveIntegerField(default=0)
    credit = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(default='NO', verbose_name='Message')

    def __str__(self) -> str:
        return str(self.description)