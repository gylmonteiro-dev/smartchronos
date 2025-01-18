from django.shortcuts import render
from accounts.models import CustomUser
from attendances.models import WorkPointRecord
# Create your views here.


def employee_list(request):
    list_employees = CustomUser.objects.all()
    return render(request, 'employee_list.html', {'list_employees': list_employees})

def list_time_records(request, pk):
    last_records = WorkPointRecord.objects.filter(user__pk=pk).order_by('-created_at')[:5]
    
    return render(request, 'time_records_list.html', {'last_records': last_records})