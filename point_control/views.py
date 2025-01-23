from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import CustomUser
from attendances.models import WorkPointRecord
from django.urls import reverse
# Create your views here.


def employee_list(request):
    list_employees = CustomUser.objects.all()
    return render(request, 'employee_list.html', {'list_employees': list_employees})

def list_time_records(request, pk):
    user = CustomUser.objects.get(pk=pk)
    last_records = WorkPointRecord.objects.filter(user__pk=pk).order_by('-created_at')[:5]
    
    return render(request, 'time_records_list.html', {'last_records': last_records, 'user': user})

def record_point_validation(request, pk):
    point_record = get_object_or_404(WorkPointRecord, pk=pk)
    point_record.valid = True
    point_record.save()

    user_pk = point_record.user.id
    return redirect(reverse("list-time-records", args=[user_pk]))

def record_point_delete(request ,pk):
    point_record = get_object_or_404(WorkPointRecord, pk=pk)
    user_pk = point_record.user.id
    point_record.delete()
    return redirect(reverse("list-time-records", args=[user_pk]))
