from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('add/', views.add_expense, name='add_expense'),
    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
    path('monthly-summary/', views.monthly_summary, name='monthly_summary'),
    path('category-monthly/', views.category_monthly_report, name='category_monthly'),
    path('charts/', views.expense_chart, name='expense_chart'),
    path('monthly-chart/', views.monthly_chart, name='monthly_chart'),

]

