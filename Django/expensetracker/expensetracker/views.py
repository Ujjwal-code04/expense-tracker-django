from django.http import HttpResponse


from django.shortcuts import render 


def home(request):
    # return HttpResponse("Welcome to the Expense Tracker Home Page!")
    return render(request,'index.html')

def add_expense(request):
    return render(request, 'add_expense.html')

def about(request):
    return HttpResponse("Welcome to the Expense Tracker about Page!")

def contact(request):
    return HttpResponse("Welcome to the Expense Tracker contact Page!")
