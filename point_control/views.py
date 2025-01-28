from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
    messages.success(request, 'Registro validado com sucesso!')
    user_pk = point_record.user.id
    return redirect(reverse("list-time-records", args=[user_pk]))

def record_point_delete(request ,pk):
    point_record = get_object_or_404(WorkPointRecord, pk=pk)
    user_pk = point_record.user.id
    point_record.delete()
    messages.success(request, 'Registro deletado com sucesso!')
    return redirect(reverse("list-time-records", args=[user_pk]))

def record_point_update(request, pk):
    
    point_record = get_object_or_404(WorkPointRecord, pk=pk)
    user_pk = point_record.user.id
    date_str = request.POST.get('date')
    time_str = request.POST.get('time')
    print(date_str, time_str)
    
    # Aqui a lógica para atualizar com base nos dados que vem do formulário a data e em seguida o horário
    if date_str and time_str:
        new_datetime_str = f'{date_str} {time_str}'
        new_datetime = datetime.strptime(new_datetime_str, "%Y-%m-%d %H:%M")
        print(new_datetime)

        point_record.update_at = new_datetime
        point_record.save()
    
    return redirect(reverse("list-time-records", args=[user_pk]))
