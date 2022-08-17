from django.contrib import admin
from expense_tracker.models import Expense, Category

# Register your models here.
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'debit', 'credit', 'category', 'description']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name',]