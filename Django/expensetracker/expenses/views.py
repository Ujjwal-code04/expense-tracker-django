from django.shortcuts import render, redirect, get_object_or_404
from django.db.models.functions import TruncMonth
from django.db.models import Sum
from .models import Expense


def home(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/home.html', {
        'expenses': expenses
    })


def add_expense(request):
    if request.method == 'POST':
        Expense.objects.create(
            title=request.POST.get('title'),
            amount=request.POST.get('amount'),
            category=request.POST.get('category'),
            date=request.POST.get('date')
        )
        return redirect('home')

    return render(request, 'add_expense.html')

def delete_expense(request, id):
    expense=get_object_or_404(Expense, id=id)
    expense.delete()
    return redirect('home')

def monthly_summary(request):
    summary = (
        Expense.objects
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('-month')
    )

    return render(request, 'monthly_summary.html', {'summary': summary})

def category_monthly_report(request):
    report = (
        Expense.objects
        .annotate(month=TruncMonth('date'))
        .values('month', 'category')
        .annotate(total=Sum('amount'))
        .order_by('-month')
    )

    return render(request, 'category_monthly.html', {'report': report})

def expense_chart(request):
    data = (
        Expense.objects
        .values('category')
        .annotate(total=Sum('amount'))
    )

    labels = [d['category'] for d in data]
    values = [d['total'] for d in data]

    return render(request, 'expenses/expense_chart.html', {
        'labels': labels,
        'values': values
    })


def monthly_chart(request):
    data = (
        Expense.objects
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )

    labels = [d['month'].strftime('%b %Y') for d in data]
    values = [float(d['total']) for d in data]

    return render(request, 'expenses/monthly_chart.html', {
    'labels': labels,
    'values': values
})
