from django.urls import path
from .views import UpdateEmployee, CreateEmployee, ViewEmployees, delete_employee

app_name = 'emp'
urlpatterns = [
    path('employee/edit/<int:pk>/', UpdateEmployee.as_view(), name='edit_employee'),
    path('employee/create/', CreateEmployee.as_view(), name='creating_employee'),
    path('employees/view/', ViewEmployees.as_view(), name='view_employees'),
    path('employees/view/ajax/delete/', delete_employee),
]
