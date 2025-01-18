from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee-list'),
    path('employees/<int:pk>/', views.list_time_records, name='list-time-records')
]
