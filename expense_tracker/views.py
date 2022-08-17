from django.shortcuts import redirect, render
from expense_tracker.models import Expense, Category
from django.contrib import messages

# Create your views here.
def home_page(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'categories' : categories,
    })    

def add_amount(request):
    if request.method == 'POST':
        amount_type = request.POST.get('amount-type')
        amount = request.POST.get('amount')
        category = request.POST.get('category')
        description = request.POST.get('description')
        if amount_type == '0' and amount and category and description:
            data = Expense.objects.create(
                debit=int(amount), credit=0, category_id=category, description=description
            )
            data.save()
            messages.success(request, 'Your debit amount added')
        elif amount_type == '1' and amount and category and description:
            data = Expense.objects.create(
                debit=0, credit=int(amount), category_id=category, description=description
            )
            data.save()
            messages.success(request, 'Your credit amount added')
    return redirect('home')

def history_page(request):
    expenses = Expense.objects.all().order_by('-id')
    debits = credits = 0
    for exp in expenses:
            debits += exp.debit
            credits += exp.credit
            # print(debits, credits)
    # print('debits :', debits, '- credits :', credits)
    balance = credits - debits
    # print('balance :', balance)
    return render(request, 'history.html', {
        'expenses' : expenses,
        'debits' : debits,
        'credits' : credits,
        'balance' : balance
    })

def report_page(request):
    date = Expense.objects.values('date')
    my_years = []
    expenses = None
    for y in date:
        temp = y['date'].year
        if temp not in my_years:
            my_years.append(temp)
    if request.method == 'POST':
        duration = request.POST.get('duration')
        year = request.POST.get('year')
        month = request.POST.get('month')
        # print(duration, year, month)
        if duration == '1' and year and month:
            print(year, month)
            expenses = Expense.objects.filter(date__year=year).filter(date__month=month).order_by('date', 'time').reverse()
        elif duration == '0' and year:
            print(year)
            expenses = Expense.objects.filter(date__year=year).order_by('date', 'time').reverse()
        return render(request, 'reports.html', {
            'my_years' : my_years,
            'expenses' : expenses
        })
    else:
        return render(request, 'reports.html', {
            'my_years' : my_years
        })