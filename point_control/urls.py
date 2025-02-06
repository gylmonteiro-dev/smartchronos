from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employee_list, name='employee-list'),
    path('employees/<int:pk>/', views.list_time_records, name='list-time-records'),
    path('employees/<int:pk>/validation/', views.record_point_validation, name='validation'),
    path('employees/<int:pk>/delete/', views.record_point_delete, name='delete-point'),
    path('employees/<int:pk>/update/', views.record_point_update, name='update-record'),
    
    # Dashboard control
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('records_by_date/', views.filter_record_by_date, name='records-by-date'),
]
